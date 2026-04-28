"""
UI Enhancement Module for Streamlit/Web Application
Contains custom UI components and styling
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, Any, Optional
import pandas as pd

def set_custom_theme():
    """Apply custom CSS and theme settings"""
    st.set_page_config(
        page_title="Crop Yield Prediction",
        page_icon="🌾",
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    h1, h2, h3 {
        color: #2E7D32;
    }
    </style>
    """, unsafe_allow_html=True)

def create_metric_card(title: str, value: Any, delta: Optional[str] = None):
    """Create a styled metric card"""
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.metric(label=title, value=value, delta=delta)
    return col1

def plot_yield_prediction(actual: pd.Series, predicted: pd.Series, 
                         crops: pd.Series = None, title: str = "Yield Prediction"):
    """Create interactive prediction plot"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(range(len(actual))),
        y=actual,
        mode='markers',
        name='Actual Yield',
        marker=dict(color='blue', size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=list(range(len(predicted))),
        y=predicted,
        mode='lines+markers',
        name='Predicted Yield',
        marker=dict(color='green', size=6),
        line=dict(dash='dash')
    ))
    
    if crops is not None:
        fig.update_layout(
            title=title,
            xaxis_title="Sample Index",
            yaxis_title="Yield (tons/hectare)",
            hovermode='closest'
        )
    
    return fig

def create_sidebar_controls():
    """Create sidebar controls for user input"""
    with st.sidebar:
        st.header("⚙️ Model Settings")
        
        model_type = st.selectbox(
            "Select Model",
            ["Random Forest", "Gradient Boosting", "Neural Network", "Linear Regression"]
        )
        
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.5,
            max_value=0.99,
            value=0.85,
            step=0.01
        )
        
        show_details = st.checkbox("Show Detailed Analysis", value=True)
        
        return {
            "model_type": model_type,
            "confidence_threshold": confidence_threshold,
            "show_details": show_details
        }

def display_results_table(data: pd.DataFrame, key_columns: list = None):
    """Display results in a styled table"""
    if key_columns:
        display_data = data[key_columns]
    else:
        display_data = data
    
    # Apply styling
    styled_df = display_data.style.background_gradient(
        subset=['predicted_yield', 'accuracy'], 
        cmap='RdYlGn'
    ).format({
        'predicted_yield': '{:.2f}',
        'accuracy': '{:.1%}'
    })
    
    st.dataframe(styled_df, use_container_width=True)