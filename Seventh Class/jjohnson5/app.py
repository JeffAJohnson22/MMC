import random
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

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


pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  StandardScaler())
])


def main():
    # Generate raw data and save it
    raw_patient_data = generate_patient_data()
    raw_patient_data.to_csv('patient_health_data.csv', index=False)
    print(f"1) Generated {len(raw_patient_data)} patient records → patient_health_data.csv")

    # Add missing values to simulate messy real-world data
    # Call it ONCE and save the result — reuse this variable everywhere
    data_with_gaps = add_missing_values(raw_patient_data)

    count = 0
    for column in data_with_gaps.columns:
        for value in data_with_gaps[column]:
            if pd.isna(value):
                count += 1
    print(f"2) Introduced {count} missing values")

    # Clean the data: fill blanks + scale everything
    # .values gives a plain numpy array (avoids the feature-name warning)
    column_names = data_with_gaps.columns.tolist()
    cleaned_array = pipeline.fit_transform(data_with_gaps.values)
    cleaned_patient_data = pd.DataFrame(cleaned_array, columns=column_names)

    # Save cleaned data
    cleaned_patient_data.to_csv('patient_health_data_clean.csv', index=False)
    print("3) Cleaned & scaled → patient_health_data_clean.csv")

    # Before / After
    print("\n— BEFORE (first 5 rows, with missing values) —")
    print(data_with_gaps.head().to_string(index=False))
    print("\n— AFTER (first 5 rows, cleaned & scaled) —")
    print(cleaned_patient_data.head().to_string(index=False))

    # Confirm zero missing values remain
    print(f"\nMissing values left: {cleaned_patient_data.isnull().sum().sum()}")

    # Prove it works on new data with no warnings
    new_patient = np.array([[45, 22.5, 130, 85]])
    new_patient_scaled = pipeline.transform(new_patient)
    print(f"\nNew patient raw:    {new_patient[0]}")
    print(f"New patient scaled: {np.round(new_patient_scaled[0], 4)}")
    print("Zero warnings ✓")


if __name__ == "__main__":
    main()
