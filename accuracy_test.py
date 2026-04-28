"""
Accuracy Testing Module
Evaluates model performance and accuracy metrics
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Any
import json
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelAccuracyTester:
    """Tests and evaluates model accuracy"""
    
    def __init__(self, model_path: str = None):
        self.model = None
        if model_path:
            self.load_model(model_path)
    
    def load_model(self, model_path: str):
        """Load trained model"""
        try:
            self.model = joblib.load(model_path)
            logger.info(f"Model loaded from {model_path}")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            self.model = None
    
    def calculate_metrics(self, y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
        """Calculate all accuracy metrics"""
        metrics = {
            'mae': mean_absolute_error(y_true, y_pred),
            'mse': mean_squared_error(y_true, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
            'r2': r2_score(y_true, y_pred),
            'mape': self.mean_absolute_percentage_error(y_true, y_pred)
        }
        
        # Additional custom metrics for agriculture
        metrics['accuracy_within_10%'] = self.percentage_within_range(y_true, y_pred, 0.10)
        metrics['accuracy_within_20%'] = self.percentage_within_range(y_true, y_pred, 0.20)
        
        return metrics
    
    def mean_absolute_percentage_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Calculate MAPE, handling zero values"""
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        # Avoid division by zero
        mask = y_true != 0
        if np.any(mask):
            return np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100
        return 0.0
    
    def percentage_within_range(self, y_true: np.ndarray, y_pred: np.ndarray, 
                               threshold: float) -> float:
        """Calculate percentage of predictions within threshold% of actual"""
        percentage_errors = np.abs((y_true - y_pred) / y_true)
        within_threshold = (percentage_errors <= threshold).sum()
        return (within_threshold / len(y_true)) * 100
    
    def cross_validation_test(self, X: pd.DataFrame, y: pd.Series, 
                            cv: int = 5) -> Dict[str, List[float]]:
        """Perform cross-validation"""
        cv_scores = cross_val_score(self.model, X, y, cv=cv, scoring='r2')
        
        return {
            'cv_scores': cv_scores.tolist(),
            'mean_score': cv_scores.mean(),
            'std_score': cv_scores.std(),
            'cv_folds': cv
        }
    
    def compare_models(self, models: Dict[str, Any], X_test: pd.DataFrame, 
                      y_test: pd.Series) -> pd.DataFrame:
        """Compare multiple models"""
        results = []
        
        for model_name, model in models.items():
            y_pred = model.predict(X_test)
            metrics = self.calculate_metrics(y_test, y_pred)
            metrics['model'] = model_name
            results.append(metrics)
        
        return pd.DataFrame(results)
    
    def create_accuracy_report(self, y_true: np.ndarray, y_pred: np.ndarray, 
                              model_name: str = "Model") -> Dict[str, Any]:
        """Generate comprehensive accuracy report"""
        metrics = self.calculate_metrics(y_true, y_pred)
        
        report = {
            'model_name': model_name,
            'metrics': metrics,
            'sample_size': len(y_true),
            'prediction_range': {
                'min_predicted': float(y_pred.min()),
                'max_predicted': float(y_pred.max()),
                'min_actual': float(y_true.min()),
                'max_actual': float(y_true.max())
            },
            'interpretation': self.interpret_metrics(metrics)
        }
        
        return report
    
    def interpret_metrics(self, metrics: Dict[str, float]) -> Dict[str, str]:
        """Provide interpretation of metrics for non-technical users"""
        interpretation = {}
        
        if metrics['r2'] >= 0.9:
            interpretation['r2'] = "Excellent fit"
        elif metrics['r2'] >= 0.7:
            interpretation['r2'] = "Good fit"
        elif metrics['r2'] >= 0.5:
            interpretation['r2'] = "Moderate fit"
        else:
            interpretation['r2'] = "Poor fit - model needs improvement"
        
        if metrics['accuracy_within_10%'] >= 80:
            interpretation['practical_accuracy'] = "Highly accurate for practical use"
        elif metrics['accuracy_within_10%'] >= 60:
            interpretation['practical_accuracy'] = "Moderately accurate"
        else:
            interpretation['practical_accuracy'] = "Needs improvement for practical use"
        
        return interpretation

# Utility functions
def plot_residuals(y_true: np.ndarray, y_pred: np.ndarray, save_path: str = None):
    """Plot residual analysis"""
    residuals = y_true - y_pred
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # Residuals vs Predicted
    axes[0].scatter(y_pred, residuals, alpha=0.5)
    axes[0].axhline(y=0, color='r', linestyle='--')
    axes[0].set_xlabel('Predicted Values')
    axes[0].set_ylabel('Residuals')
    axes[0].set_title('Residuals vs Predicted')
    
    # Histogram of residuals
    axes[1].hist(residuals, bins=30, edgecolor='black')
    axes[1].set_xlabel('Residuals')
    axes[1].set_ylabel('Frequency')
    axes[1].set_title('Distribution of Residuals')
    
    # Q-Q plot
    from scipy import stats
    stats.probplot(residuals, dist="norm", plot=axes[2])
    axes[2].set_title('Q-Q Plot')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def save_accuracy_report(report: Dict[str, Any], filepath: str):
    """Save accuracy report to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(report, f, indent=2)
    logger.info(f"Accuracy report saved to {filepath}")