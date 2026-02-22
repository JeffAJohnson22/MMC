"""
Project #6: The Classifier Showdown
Name: Jeff Johnson
Date: 02/23/2026
"""

import os
import random
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Creates 500 patients with age, bmi, and blood sugar
def generate_patient_data():
    df = pd.DataFrame({
        'age': np.random.randint(18, 90, 500),
        'bmi': np.random.normal(26, 6, 500),
        'blood_sugar': np.random.normal(105, 25, 500)
    })
    return df

def main():
    raw_patient_data = generate_patient_data()
    
    # Create diagnosis classification based on risk logic
    risk_logic = (raw_patient_data['age'] * 0.3) + (raw_patient_data['bmi'] * 1.2) + (raw_patient_data['blood_sugar'] * 0.2)
    raw_patient_data['diagnosis'] = (risk_logic > 75).astype(int)
    
    print("Sample of Generated Patient Data:")
    print(raw_patient_data.head())
    
    # Save to CSV in current working directory
    csv_filename = "classifier_patient_data.csv"
    raw_patient_data.to_csv(csv_filename, index=False)
    print(f"\nPatient data saved to {csv_filename}")
    
    # Separate features and target
    X = raw_patient_data[['age', 'bmi', 'blood_sugar']]
    y = raw_patient_data['diagnosis']
    
    # Scale features using StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform 80/20 train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    print(f"\nFeature scaling and train-test split completed:")
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    
    # Train three classification models
    print("\n=== Training Classification Models ===")
    
    # Decision Tree Classifier
    dt_classifier = DecisionTreeClassifier(max_depth=3)
    dt_classifier.fit(X_train, y_train)
    print("Decision Tree Classifier trained")
    
    # Random Forest Classifier
    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)
    print("Random Forest Classifier trained")
    
    # k-Nearest Neighbors Classifier
    knn_classifier = KNeighborsClassifier()
    knn_classifier.fit(X_train, y_train)
    print("k-Nearest Neighbors Classifier trained")
    
    # Make predictions on test set
    print("\n=== Model Accuracy Scores ===")
    
    dt_predictions = dt_classifier.predict(X_test)
    dt_accuracy = accuracy_score(y_test, dt_predictions)
    print(f"Decision Tree Accuracy: {dt_accuracy:.4f}")
    
    rf_predictions = rf_classifier.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_predictions)
    print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
    
    knn_predictions = knn_classifier.predict(X_test)
    knn_accuracy = accuracy_score(y_test, knn_predictions)
    print(f"k-Nearest Neighbors Accuracy: {knn_accuracy:.4f}")
    
if __name__ == "__main__":
    main()
