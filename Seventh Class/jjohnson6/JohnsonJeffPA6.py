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
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

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
    
if __name__ == "__main__":
    main()
