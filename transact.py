import pandas as pd
import web3
import contract

# Load and clean CSV data
csv_file = "healthcare_data.csv"
df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip().str.lower()

# Fill missing values with safe defaults
df['ecg_peak_count'] = df['ecg_peak_count'].fillna(0).astype(int)
df['ecg_signal_strength'] = df['ecg_signal_strength'].fillna(0).astype(int)
df['oxygen_level'] = df['oxygen_level'].fillna(0).astype(int) 
df['body_temp'] = df['body_temp'].fillna(0).astype(int)
df['hasecg'] = df['hasecg'].fillna(False).astype(bool)

# Loop through and send transactions
for index, row in df.iterrows():
    tx_hash = contract.functions.addRecord(
        row['patient_id'],
        row['heart_rate'],
        row['blood_pressure'],
        row['oxygen_level'],
        row['body_temp'],
        row['ecg_peak_count'],
        row['ecg_signal_strength'],
        row['hasecg']
    ).transact()

    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Record {index+1} added with transaction hash: {tx_hash.hex()}")