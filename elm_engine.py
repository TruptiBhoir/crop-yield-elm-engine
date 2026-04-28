import numpy as np
from typing import Union, Optional

class ELM:
    """
    Extreme Learning Machine (ELM) for Regression.
    
    A Single-hidden Layer Feedforward Network (SLFN) where input weights 
    are randomly assigned and output weights are analytically determined.
    """

    def __init__(self, input_size: int, hidden_neurons: int, random_state: int = 3):
        """
        Initializes the ELM model with random weights and biases.
        
        Args:
            input_size (int): Number of input features.
            hidden_neurons (int): Number of neurons in the hidden layer.
            random_state (int): Seed for reproducibility.
        """
        self.input_size = input_size
        self.hidden_neurons = hidden_neurons
        np.random.seed(random_state)
        
        # Randomly initialize weights and biases
        self.input_weights = np.random.randn(self.input_size, self.hidden_neurons)
        self.bias = np.random.randn(self.hidden_neurons)
        self.output_weights = None

    def _activation(self, x: np.ndarray) -> np.ndarray:
        """Sigmoid activation function."""
        return 1.0 / (1.0 + np.exp(-x))

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Trains the ELM model using the Moore-Penrose pseudoinverse.
        
        Args:
            X (np.ndarray): Training features of shape (n_samples, n_features).
            y (np.ndarray): Target values of shape (n_samples,).
        """
        y = np.array(y).reshape(-1, 1) if y.ndim == 1 else y
        
        # Calculate hidden layer output matrix (H)
        H = self._activation(np.dot(X, self.input_weights) + self.bias)
        
        # Calculate output weights using pseudoinverse: Beta = H+ * Y
        H_pinv = np.linalg.pinv(H)
        self.output_weights = np.dot(H_pinv, y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts target values for given inputs.
        
        Args:
            X (np.ndarray): Input features.
            
        Returns:
            np.ndarray: Flattened array of predicted values.
        """
        if self.output_weights is None:
            raise ValueError("Model must be fitted before predicting.")
            
        H = self._activation(np.dot(X, self.input_weights) + self.bias)
        y_pred = np.dot(H, self.output_weights)
        return y_pred.ravel()