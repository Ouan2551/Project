# Essential ML Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

# Dataset Loading
def load_dataset():
    # Example: Using Iris dataset
    from sklearn.datasets import load_iris
    data = load_iris()
    X = data.data
    y = data.target
    return X, y

# Data Preprocessing
def preprocess_data(X, y):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test

# Model Training
def train_model(X_train, y_train):
    # Random Forest Classifier
    model = RandomForestClassifier(
        n_estimators=100, 
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

# Model Evaluation
def evaluate_model(model, X_test, y_test):
    # Predictions
    y_pred = model.predict(X_test)
    
    # Performance metrics
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Accuracy: {accuracy}")
    print("Classification Report:\n", report)

# Feature Importance
def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.title("Feature Importances")
    plt.bar(range(len(importances)), importances[indices])
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45)
    plt.tight_layout()
    plt.show()

# Main Execution
def main():
    # Load Dataset
    X, y = load_dataset()
    
    # Preprocessing
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    
    # Model Training
    model = train_model(X_train, y_train)
    
    # Evaluation
    evaluate_model(model, X_test, y_test)
    
    # Feature Importance
    from sklearn.datasets import load_iris
    iris_data = load_iris()
    plot_feature_importance(model, iris_data.feature_names)

# Run the script
if __name__ == "__main__":
    main()