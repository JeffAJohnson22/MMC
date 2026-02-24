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
    X = raw_patient_data[['age', 'bmi', 'blood_sugar']]
    y = raw_patient_data['diagnosis']

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 80/20 train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Train three classification models
    dt_classifier = DecisionTreeClassifier(max_depth=3)
    dt_classifier.fit(X_train, y_train)

    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)

    knn_classifier = KNeighborsClassifier()
    knn_classifier.fit(X_train, y_train)

    # Evaluate accuracy
    dt_accuracy = accuracy_score(y_test, dt_classifier.predict(X_test))
    rf_accuracy = accuracy_score(y_test, rf_classifier.predict(X_test))
    knn_accuracy = accuracy_score(y_test, knn_classifier.predict(X_test))

    print("=" * 30)
    print("Model Accuracy Results")
    print("=" * 30)
    print()
    print(f"Optimal Tree  -> Accuracy: {dt_accuracy:.2f}")
    print(f"Random Forest -> Accuracy: {rf_accuracy:.2f}")
    print(f"K-NN (k=5)    -> Accuracy: {knn_accuracy:.2f}")

    # Visualize model logic
    print("\n[SYSTEM] Visualizing model logic... (Close the plot window to continue to input)")

    feature_names = ['Age', 'BMI', 'Blood Sugar']
    feature_importance = dt_classifier.feature_importances_
    plt.figure(figsize=(24,10))

    # Graph A Feature Importance
    plt.subplot(1, 2, 1)
    plt.barh(feature_names, feature_importance, color=["#1f38b4", "#00ca65", "#d80303"])
    plt.title('Feature Importance')
    plt.xlabel('Importance')
    plt.grid(axis='x', alpha=0.3)

    # Graph B Tree Structure
    plt.subplot(1, 2, 2)
    plot_tree(dt_classifier, feature_names=feature_names, class_names=['No Risk', 'Risk'], filled=True)
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
        patient_df = pd.DataFrame({
            'age': [age],
            'bmi': [bmi],
            'blood_sugar': [blood_sugar]
        })
        patient = scaler.transform(patient_df)
        labels = {0: "Healthy", 1: "At Risk"}

        dt_vote = dt_classifier.predict(patient)[0]
        rf_vote = rf_classifier.predict(patient)[0]
        knn_vote = knn_classifier.predict(patient)[0]

        print(f"\n[Voting Results]")
        print(f"Decision Tree: {labels[dt_vote]}")
        print(f"Random Forest: {labels[rf_vote]}")
        print(f"K-NN (k=5):    {labels[knn_vote]}")
    except ValueError:
        print("Invalid input. Needs to be a number.")

if __name__ == "__main__":
    main()
