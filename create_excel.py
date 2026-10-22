# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Yukta Kulkarni]
# Admin PRN: [1302250198]
# File 2: Generates 'ml_input_data.xlsx'
# ==============================================================================

import pandas as pd

data = {
    "Txn_ID": ["TX101", "TX102", "TX103", "TX104", "TX105"],
    "Amount_INR": [15000, 75000, 4000, 120000, 60000],
    "Is_International": [0, 1, 0, 1, 0], # 1 = Yes, 0 = No
    "Failed_Attempts": [0, 3, 1, 4, 0],
    "Is_Fraud": [0, 1, 0, 1, 0]          # 1 = Fraud, 0 = Legit
}

df = pd.DataFrame(data)
df.to_excel("fraud_detection_inputs.xlsx", index=False)
print("Data generated successfully: fraud_detection_inputs.xlsx")
