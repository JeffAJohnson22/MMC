"""
Project #6: The Classifier Showdown
Name: Jeff Johnson
Date: 02/23/2026
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
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

    # Save to CSV
    csv_filename = "classifier_patient_data.csv"
    raw_patient_data.to_csv(csv_filename, index=False)

    # Separate features and target
    valueX = raw_patient_data[['age', 'bmi', 'blood_sugar']]
    valueY = raw_patient_data['diagnosis']

    # Scale the features
    scaler = StandardScaler()
    xScaled = scaler.fit_transform(valueX)

    # 80/20 train-test split
    trainValueX, testValueX, trainValueY, testValueY = train_test_split(xScaled, valueY, test_size=0.2, random_state=42)

    # Train three classification models
    dtValue = DecisionTreeClassifier(max_depth=3)
    dtValue.fit(trainValueX, trainValueY)

    rfValue = RandomForestClassifier()
    rfValue.fit(trainValueX, trainValueY)
    
    knnValue = KNeighborsClassifier()
    knnValue.fit(trainValueX, trainValueY)

    # Evaluate accuracy
    dtAccuracy = accuracy_score(testValueY, dtValue.predict(testValueX))
    rfAccuracy = accuracy_score(testValueY, rfValue.predict(testValueX))
    knnAccuracy = accuracy_score(testValueY, knnValue.predict(testValueX))

    print("=" * 30)
    print("Model Accuracy Results")
    print("=" * 30)
    print()
    print(f"Optimal Tree  -> Accuracy: {dtAccuracy:.2f}")
    print(f"Random Forest -> Accuracy: {rfAccuracy:.2f}")
    print(f"K-NN (k=5)    -> Accuracy: {knnAccuracy:.2f}")

    # Visualize model logic
    print("\n[SYSTEM] Visualizing model logic... (Close the plot window to continue to input)")

    feature_names = ['Age', 'BMI', 'Blood Sugar']
    feature_importance = dtValue.feature_importances_
    plt.figure(figsize=(24,10))

    # Graph A Feature Importance
    plt.subplot(1, 2, 1)
    plt.barh(feature_names, feature_importance, color=["#1f38b4", "#00ca65", "#d80303"])
    plt.title('Feature Importance')
    plt.xlabel('Importance')
    plt.grid(axis='x', alpha=0.3)

    # Graph B Tree Structure
    plt.subplot(1, 2, 2)
    plot_tree(dtValue, feature_names=feature_names, class_names=['No Risk', 'Risk'], filled=True)
    plt.title('Decision Tree Structure')

    plt.show()

    print("\n" + "="*30)
    print("New Patient Diagnosis")
    print("=" * 30)
    
    try:
        # loop to get user input for new patient data
        age = float(input("Enter Age: "))
        bmi = float(input("Enter BMI: "))
        blood_sugar = float(input("Enter Blood Sugar: "))

        # Create patient DataFrame with feature names
        patientData = pd.DataFrame({
            'age': [age],
            'bmi': [bmi],
            'blood_sugar': [blood_sugar]
        })
        patient = scaler.transform(patientData)
        labels = {0: "Healthy", 1: "At Risk"}

        dtPatientValue = dtValue.predict(patient)[0]
        rfPatientValue = rfValue.predict(patient)[0]
        knnPatientValue = knnValue.predict(patient)[0]

        print(f"\n[Voting Results]")
        print(f"Decision Tree: {labels[dtPatientValue]}")
        print(f"Random Forest: {labels[rfPatientValue]}")
        print(f"K-NN (k=5):    {labels[knnPatientValue]}")
    except ValueError:
        print("Invalid input. Needs to be a number.")

if __name__ == "__main__":
    main()
