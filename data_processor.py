import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib

print(" Step 1: Data Preprocessing")
print("=" * 50)

# Load dataset
df = pd.read_csv("crop_yield_dataset.csv")
print(f" Dataset loaded: {df.shape}")

# Basic cleaning
df = df.dropna()
print(f" After cleaning: {df.shape}")

# Encode categorical variables
le_crop = LabelEncoder()
le_soil = LabelEncoder()

df['Crop_Type_encoded'] = le_crop.fit_transform(df['Crop_Type'])
df['Soil_Type_encoded'] = le_soil.fit_transform(df['Soil_Type'])

print(" Categorical variables encoded")

# Select features (using original columns from your dataset)
feature_columns = [
    'Crop_Type_encoded', 'Soil_Type_encoded', 'Soil_pH', 
    'Temperature', 'Humidity', 'Wind_Speed', 'N', 'P', 'K', 'Soil_Quality'
]

X = df[feature_columns]
y = df['Crop_Yield']

print(f" Features selected: {len(feature_columns)}")
print(f" Target variable: Crop_Yield")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f" Train set: {X_train.shape}")
print(f" Test set: {X_test.shape}")

# Scale features
scaler_X = StandardScaler()
X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled = scaler_X.transform(X_test)

print(" Features scaled")

# Convert y to numpy arrays to avoid pandas Series issues
y_train_values = y_train.values
y_test_values = y_test.values

print(" Target variables converted to numpy arrays")

# Save preprocessing objects
preprocessing_data = {
    'scaler_X': scaler_X,
    'feature_columns': feature_columns,
    'le_crop': le_crop,
    'le_soil': le_soil,
    'X_train_scaled': X_train_scaled,
    'X_test_scaled': X_test_scaled,
    'y_train': y_train_values,  # Store as numpy array
    'y_test': y_test_values    # Store as numpy array
}

joblib.dump(preprocessing_data, 'preprocessing_data.pkl')

print(" Preprocessing data saved to 'preprocessing_data.pkl'")
print(" Data preprocessing completed successfully!")