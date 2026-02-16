import random
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings("ignore")

def generate_patient_data():
    patients = []

    for _ in range(500):
        age = random.randint(18, 100)
        bmi = round(random.uniform(15.0, 30.0), 1)
        blood_sugar_level = random.randint(50, 315)

        if age < 35:          history_points = 0
        elif age < 44:        history_points = 3
        elif age < 60:        history_points = 5
        else:                 history_points = 7

        if bmi < 18.5:        history_points += 0
        elif bmi < 25:        history_points += 3
        elif bmi < 30:        history_points += 5
        else:                  history_points += 7

        if blood_sugar_level < 100:    history_points += 0
        elif blood_sugar_level < 126:  history_points += 3
        elif blood_sugar_level < 200:  history_points += 5
        else:                          history_points += 7

        history_points = max(history_points, 1)
        health_risk_score = age + bmi + round(blood_sugar_level / history_points)

        patients.append({
            'age': age,
            'bmi': bmi,
            'blood_sugar_level': blood_sugar_level,
            'health_risk_score': health_risk_score
        })

    return pd.DataFrame(patients)


def add_missing_values(patient_data, missing_fraction=0.05):
    patient_data = patient_data.copy()
    for column in patient_data.columns:
        rows_to_blank = random.sample(range(len(patient_data)), int(len(patient_data) * missing_fraction))
        patient_data.loc[rows_to_blank, column] = np.nan
    return patient_data


def main():
    raw_patient_data = generate_patient_data()
    raw_patient_data.to_csv('patient_health_data.csv', index=False)

    # Add missing values to simulate messy real-world data
    data_with_gaps = add_missing_values(raw_patient_data)

    count = 0
    for column in data_with_gaps.columns:
        for value in data_with_gaps[column]:
            if pd.isna(value):
                count += 1

    
    # Imputation is going to fill up the missing values with a median
    # So no empty cells break the model
    imputer = SimpleImputer(strategy='median')
    data_imputed = imputer.fit_transform(data_with_gaps)
    
    # Standardization will scale whatever value to a relative number
    # So that one value doesnt dominate the model just because its larger
    scaler = StandardScaler()
    data_standardized = scaler.fit_transform(data_imputed)
    
    # Convert back to DataFrame with original column names
    column_names = data_with_gaps.columns.tolist()
    cleaned_patient_data = pd.DataFrame(data_standardized, columns=column_names)

    # Save cleaned data
    cleaned_patient_data.to_csv('patient_health_data_clean.csv', index=False)
    
    # Prepare data for modeling
    patient_features = cleaned_patient_data[['age', 'bmi', 'blood_sugar_level']].values
    health_risk_scores = cleaned_patient_data['health_risk_score'].values
    
    # Split up the data into training and testing sets (80/20 split)
    features_train, features_test, risk_scores_train, risk_scores_test = train_test_split(patient_features, health_risk_scores, test_size=0.2, random_state=42)
    
    # Make a new scaler so the 3 input features are good for the model
    feature_scaler = StandardScaler()
    features_train_scaled = feature_scaler.fit_transform(features_train)
    features_test_scaled = feature_scaler.transform(features_test)
    
    age_train = []
    for row in features_train_scaled:
        age_train.append([row[0]])
    age_train = np.array(age_train)
    
    age_test = []
    for row in features_test_scaled:
        age_test.append([row[0]])
    age_test = np.array(age_test)
    
    underfit_model = LinearRegression()
    underfit_model.fit(age_train, risk_scores_train)
    predictions_underfit = underfit_model.predict(age_test)
    
    mse_underfit = mean_squared_error(risk_scores_test, predictions_underfit)
    r2_underfit = r2_score(risk_scores_test, predictions_underfit)

    # Overfit (High Variance): A model using PolynomialFeatures with a degree of 10 or higher.
    poly = PolynomialFeatures(degree=10)
    features_train_polynomial = poly.fit_transform(features_train_scaled)
    features_test_polynomial = poly.transform(features_test_scaled)
    
    overfit_model = LinearRegression()
    overfit_model.fit(features_train_polynomial, risk_scores_train)
    predictions_overfit = overfit_model.predict(features_test_polynomial)
    
    mse_overfit = mean_squared_error(risk_scores_test, predictions_overfit)
    r2_overfit = r2_score(risk_scores_test, predictions_overfit)
    
    optimal_model = LinearRegression()
    optimal_model.fit(features_train_scaled, risk_scores_train)
    predictions_optimal = optimal_model.predict(features_test_scaled)
    
    mse_optimal = mean_squared_error(risk_scores_test, predictions_optimal)
    r2_optimal = r2_score(risk_scores_test, predictions_optimal)
    
    print("\n" + "="*30)
    print("Model Performance Metrics")
    print("="*30)
    print(f"Underfit (High Bias) -> MSE: {mse_underfit:.2f} | R2: {r2_underfit:.2f}")
    print(f"Optimal Model        -> MSE: {mse_optimal:.2f}  | R2: {r2_optimal:.2f}")
    print(f"Overfit (High Var)   -> MSE: {mse_overfit:.2f}  | R2: {r2_overfit:.2f}")
        
    # Save the scaler for preprocessing new data
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(feature_scaler, f)
    
    # Save the optimal model
    with open('optimal_model.pkl', 'wb') as f:
        pickle.dump(optimal_model, f)
    
    # Train a Logistic Regression model for risk probability
    # Create binary labels for logistic regression
    median_risk = np.median(health_risk_scores)
    risk_binary_train = (risk_scores_train > median_risk).astype(int)
    
    logistic_model = LogisticRegression(random_state=42, max_iter=1000)
    logistic_model.fit(features_train_scaled, risk_binary_train)
    
    with open('logistic_model.pkl', 'wb') as f:
        pickle.dump(logistic_model, f)

    print("\n" + "="*30)
    print("New Patient Inference")
    print("="*30 + "\n")
    
    while True:
        try:
            age = float(input("Enter patient age: "))
            bmi = float(input("Enter patient BMI: "))
            blood_sugar = float(input("Enter patient blood sugar level: "))
            
            # Validate inputs
            if not (18 <= age <= 100):
                print("Age must be between 18 and 100")
                continue
            if not (15.0 <= bmi <= 30.0):
                print("BMI must be between 15.0 and 30.0")
                continue
            if not (50 <= blood_sugar <= 315):
                print("Blood Sugar Level must be between 50 and 315")
                continue
            
            # Preprocess new patient data
            patient_input = np.array([[age, bmi, blood_sugar]])
            patient_input_scaled = feature_scaler.transform(patient_input)
            
            # Get predictions from optimal model
            predicted_risk_raw = optimal_model.predict(patient_input_scaled)[0]
            
            # Normalize health_risk_score to 0-100 scale using fixed clinical boundaries
            # Clinical scale: 50 = minimum risk, 200 = maximum risk
            minimum_risk_threshold = 50
            maximum_risk_threshold = 200
            health_risk_normalized = max(0, min(100, ((predicted_risk_raw - minimum_risk_threshold) / (maximum_risk_threshold - minimum_risk_threshold)) * 100))
            
            # Get risk probability from logistic model
            risk_probability = logistic_model.predict_proba(patient_input_scaled)[0][1] * 100
            
            # Determine diagnosis based on 60-point threshold
            diagnosis = "is at risk" if health_risk_normalized >= 60 else "is healthy"
            
            # Display results
            print("\n" + "="*30)
            print("Patient Health Risk Assessment")
            print("="*30)
            print(f"Patient: Age={age}, BMI={bmi}, Blood Sugar={blood_sugar}")
            print(f"\nPredicted Health Risk Score: {health_risk_normalized:.2f}/100")
            print(f"Probability of Risk: {risk_probability:.2f}%")
            print(f"\n Diagnosis: {diagnosis}")
            print(f"Threshold: 60 points | Patient Score: {health_risk_normalized:.2f}")
            print("="*30)
            
        except ValueError as e:
            print(f"Invalid input: {str(e)}")
            continue
        except Exception as e:
            print(f"Error: {type(e).__name__}: {str(e)}")
            continue
        
        # Ask if user wants to assess another patient
        another = input("\nAssess another patient? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            print("\n End of Program.")
            break

if __name__ == "__main__":
    main()
