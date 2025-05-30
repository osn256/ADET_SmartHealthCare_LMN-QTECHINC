import pandas as pd
import web3
import contract

for i in range(200):  # 201 is the actual number of records (Pls replace with the correct number if different)
    record = contract.functions.getRecord(i).call()
    print(f"🩺 Record {i}:")
    print(f"  Timestamp: {record[0]}")
    print(f"  Patient ID: {record[1]}")
    print(f"  Heart Rate: {record[2]}")
    print(f"  Blood Pressure: {record[3]}")
    print(f"  Oxygen Level: {record[4]}")
    print(f"  Body Temp: {record[5]}")
    print(f"  ECG Peak Count: {record[6]}")
    print(f"  ECG Signal Strength: {record[7]}")
    print(f"  Has ECG: {record[8]}")