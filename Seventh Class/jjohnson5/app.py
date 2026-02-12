import csv
import random

def generate_patient_data():    
    patients = []
    
    for _ in range(1, 501):
        # Generate age (18-100 years)
        age = random.randint(18, 100)
        
        # Generate BMI (15.0-30.0)
        bmi = round(random.uniform(15.0, 30.0), 1)
        
        # Generate blood sugar level (50-315 mg/dL)
        blood_sugar_level = random.randint(50, 315)
        
        # Generate Health Risk Score      
        if age < 35:
            history_points = 0 
        elif 35 <= age < 44:
            history_points = 3
        elif 45 <= age < 60:
            history_points = 5
        else:            
            history_points = 7 
            
        if bmi < 18.5:
            history_points += 0
        elif 18.5 <= bmi < 25:
            history_points += 3
        elif 25 <= bmi < 30:
            history_points += 5
        else:
            history_points += 7
            
        if blood_sugar_level < 100:
            history_points += 0
        elif 100 <= blood_sugar_level < 126:
            history_points += 3
        elif 126 <= blood_sugar_level < 200:
            history_points += 5
        else:           
            history_points += 7
        
        history_points = max(history_points, 1)
            
        health_risk_score = age + bmi+ (blood_sugar_level/history_points).__round__()
                
        # Create patient record
        patient = {
            'age': age,
            'bmi': bmi,
            'blood_sugar_level': blood_sugar_level,
            'health_risk_score': health_risk_score
        }
        
        patients.append(patient)
    
    return patients

def save_to_csv(patients, filename='patient_health_data.csv'):
    fieldnames = patients[0].keys()
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)
        
def main():
    patients = generate_patient_data()
    save_to_csv(patients)

if __name__ == "__main__":
    main()
