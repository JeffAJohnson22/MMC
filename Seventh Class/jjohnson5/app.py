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

# Creates 500 fake patients with age, bmi, blood sugar, and a risk score
def generate_patient_data():
    patients = []

    for _ in range(500):
        age = random.randint(18, 100)
        bmi = round(random.uniform(10.0, 60.0), 1)
        blood_sugar_level = random.randint(50, 315)

        # Risk score is built from all three features
        age_points = age // 2
        bmi_points = bmi * 2
        sugar_points = blood_sugar_level // 7

        health_risk_score = round(age_points + bmi_points + sugar_points)

        patients.append({
            'age': age,
            'bmi': bmi,
            'blood_sugar_level': blood_sugar_level,
            'health_risk_score': health_risk_score
        })

    return pd.DataFrame(patients)

# Randomly blanks out 5% of values in each column to simulate messy data
def add_missing_values(patient_data, missing_fraction=0.05):
    patient_data = patient_data.copy()
    for column in patient_data.columns:
        rows_to_blank = random.sample(range(len(patient_data)), int(len(patient_data) * missing_fraction))
        patient_data.loc[rows_to_blank, column] = np.nan
    return patient_data

# Cleans the data: fills missing values with median
def clean_data(raw_data):
    # Add missing values to simulate real world data
    data_with_gaps = add_missing_values(raw_data)

    # Fill missing values with the median of each column
    imputer = SimpleImputer(strategy='median')
    column_names = data_with_gaps.columns.tolist()
    data_imputed = pd.DataFrame(imputer.fit_transform(data_with_gaps), columns=column_names)

    # Save and return the imputed data at raw scale so train_models handles its own scaling
    data_imputed.to_csv('patient_health_data_clean.csv', index=False)
    return data_imputed

# Trains 3 models to show bias-variance tradeoff, plus a logistic model for classification
def train_models(data_imputed):
    # X = features, y = target
    patient_features = data_imputed[['age', 'bmi', 'blood_sugar_level']]
    health_risk_scores = data_imputed['health_risk_score'].values

    # 80% train, 20% test
    features_train, features_test, risk_scores_train, risk_scores_test = train_test_split(
        patient_features, health_risk_scores, test_size=0.2, random_state=42
    )

    # Scale features for modeling
    feature_scaler = StandardScaler()
    features_train_scaled = feature_scaler.fit_transform(features_train)
    features_test_scaled = feature_scaler.transform(features_test)

    # Underfit model (high bias): only uses age, too simple to learn the full pattern 
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

    # Overfit model (high variance): degree-10 polynomial, memorizes noise 
    poly = PolynomialFeatures(degree=10)
    features_train_poly = poly.fit_transform(features_train_scaled)
    features_test_poly = poly.transform(features_test_scaled)

    overfit_model = LinearRegression()
    overfit_model.fit(features_train_poly, risk_scores_train)
    predictions_overfit = overfit_model.predict(features_test_poly)

    mse_overfit = mean_squared_error(risk_scores_test, predictions_overfit)
    r2_overfit = r2_score(risk_scores_test, predictions_overfit)

    # Optimal model/balanced: all 3 features, plain linear regression 
    optimal_model = LinearRegression()
    optimal_model.fit(features_train_scaled, risk_scores_train)
    predictions_optimal = optimal_model.predict(features_test_scaled)

    mse_optimal = mean_squared_error(risk_scores_test, predictions_optimal)
    r2_optimal = r2_score(risk_scores_test, predictions_optimal)

    # Logistic regression: classifies patients as above or below median risk 
    median_risk = np.median(health_risk_scores)
    risk_binary_train = (risk_scores_train > median_risk).astype(int)  # 1 = high risk, 0 = low

    logistic_model = LogisticRegression(random_state=42, max_iter=1000)
    logistic_model.fit(features_train_scaled, risk_binary_train)

    # Print comparison of all three models
    print("\n" + "="*30)
    print("Model Performance Metrics")
    print("="*30)
    print(f"Underfit (High Bias) -> MSE: {mse_underfit:.2f} | R2: {r2_underfit:.2f}")
    print(f"Optimal Model        -> MSE: {mse_optimal:.2f}  | R2: {r2_optimal:.2f}")
    print(f"Overfit (High Var)   -> MSE: {mse_overfit:.2f}  | R2: {r2_overfit:.2f}")

    # Save min/max to normalize future predictions to 0-100
    risk_min = health_risk_scores.min()
    risk_max = health_risk_scores.max()

    return feature_scaler, optimal_model, logistic_model, risk_min, risk_max

# Asks the user for age, bmi, and blood sugar
def get_patient_input():
    age = float(input("Enter patient age (18 to 100): "))
    if not (18 <= age <= 100):
        print("Invalid. Age must be between 18 and 100.")
        return None

    bmi = float(input("Enter patient BMI (10.0 to 60.0): "))
    if not (10.0 <= bmi <= 60.0):
        print("Invalid. BMI must be between 10.0 and 60.0.")
        return None

    blood_sugar = float(input("Enter patient blood sugar level (50 to 315): "))
    if not (50 <= blood_sugar <= 315):
        print("Invalid. Blood sugar must be between 50 and 315.")
        return None

    return age, bmi, blood_sugar

# Scales input, runs both models, and returns a score, probability, and diagnosis
def predict_risk(age, bmi, blood_sugar, feature_scaler,
                 optimal_model, logistic_model, risk_min, risk_max):
    # Scale input the same way training data was scaled (DataFrame preserves feature names)
    patient_input = pd.DataFrame([[age, bmi, blood_sugar]], columns=['age', 'bmi', 'blood_sugar_level'])
    patient_input_scaled = feature_scaler.transform(patient_input)

    # Get risk score and normalize to 0 to 100
    predicted_risk_raw = optimal_model.predict(patient_input_scaled)[0]
    health_risk_normalized = max(0, min(100, ((predicted_risk_raw - risk_min) / (risk_max - risk_min)) * 100))

    # Get probability of being high risk from logistic model
    risk_probability = logistic_model.predict_proba(patient_input_scaled)[0][1] * 100

    # At risk if either score hits 60 otherwise healthy
    if health_risk_normalized >= 60 or risk_probability >= 60:
        diagnosis = "AT RISK"
    else:
        diagnosis = "HEALTHY"

    return health_risk_normalized, risk_probability, diagnosis

# Prints the final results
def display_results(age, bmi, blood_sugar, health_risk_normalized, risk_probability, diagnosis):
    print("\n" + "="*30)
    print("Patient Health Risk Assessment")
    print("="*30)
    print(f"Patient: Age={age}, BMI={bmi}, Blood Sugar={blood_sugar}")
    print(f"\nPredicted Health Risk Score: {health_risk_normalized:.2f}/100")
    print(f"Probability of Risk: {risk_probability:.2f}%")
    print(f"\nDiagnosis: {diagnosis}")
    print("="*30)

# Loops asking for patients until the user stops
def the_interface(feature_scaler, optimal_model, logistic_model, risk_min, risk_max):
    print("\n" + "="*30)
    print("New Patient Inference")
    print("="*30 + "\n")

    while True:
        try:
            patient_input = get_patient_input()
            if patient_input is None:
                continue

            age, bmi, blood_sugar = patient_input

            health_risk_normalized, risk_probability, diagnosis = predict_risk(
                age, bmi, blood_sugar, feature_scaler, optimal_model, logistic_model,
                risk_min, risk_max
            )

            display_results(age, bmi, blood_sugar, health_risk_normalized, risk_probability, diagnosis)

        except ValueError as e:
            print(f"Invalid input: {str(e)}")
            continue
        except Exception as e:
            print(f"Error: {type(e).__name__}: {str(e)}")
            continue

        another = input("\nAssess another patient? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            print("\n End of Program.")
            break


def main():
    # Load or generate raw patient data
    if os.path.exists('patient_health_data.csv'):
        raw_patient_data = pd.read_csv('patient_health_data.csv')
    else:
        raw_patient_data = generate_patient_data()
        raw_patient_data.to_csv('patient_health_data.csv', index=False)

    # Load or clean the data
    if os.path.exists('patient_health_data_clean.csv'):
        data_imputed = pd.read_csv('patient_health_data_clean.csv')
    else:
        data_imputed = clean_data(raw_patient_data)

    # Train all models and print metrics
    feature_scaler, optimal_model, logistic_model, risk_min, risk_max = train_models(data_imputed)

    # Start the interactive patient assessment loop
    the_interface(feature_scaler, optimal_model, logistic_model, risk_min, risk_max)

if __name__ == "__main__":
    main()
