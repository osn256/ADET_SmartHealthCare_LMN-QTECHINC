import pandas as pd                             # Import  
import numpy as np
from datetime import datetime, timedelta

num_records = 200  # Adjust this number as needed

# Example for Smart Healthcare Monitoring
data = []

for _ in range(num_records):
    # Decide randomly whether to include ECG data (e.g., 60% chance)
    include_ecg = np.random.rand() < 0.4

    record = {
        "timestamp": datetime.now() - timedelta(minutes=np.random.randint(0, 1440)),        # Random timestamp in the last 24 hours
        "patient_id": f"PAT{np.random.randint(100, 999)}",                                  # Random patient ID
        "heart_rate": str(np.random.randint(60, 100)) + "bpm",                              # Normal heart rate range
        "blood_pressure": f"{np.random.randint(100, 140)}/{np.random.randint(60, 90)}",     # Systolic/Diastolic range
        "oxygen_level": np.random.randint(95, 100),                                         # Oxygen saturation in normal range
        "body_temp": round(np.random.uniform(36.0, 38.0), 1),                               # Body temperature in Celsius
        "ECG_signal_strength": round(np.random.uniform(0.8, 1.0), 2) if include_ecg else None,  # 
        "ECG_peak_count": np.random.randint(12, 20) if include_ecg else None,               #   
    }
    data.append(record)

# Convert to DataFrame
df = pd.DataFrame(data) 

# Save dataset
df.to_csv("healthcare_data.csv", index=False)           # 
df.to_json("healthcare_data.json", orient="records")    # 

# Display first few rows
print(df.head())
print("Dataset saved as healthcare_data.csv and healthcare_data.json")
print("Sample data:")

pd.read_csv("healthcare_data.csv").head()  # Display first few rows of the CSV file
