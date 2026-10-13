# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shlok Shirke]
# Admin PRN: [1302250028]
# File 2: Generates 'ml_input_data.xlsx'
# ==============================================================================
import pandas as pd

data = {
    "Customer_Name": [
        "Aarav Sharma",
        "Rohan Mehta",
        "Priya Verma",
        "Ananya Iyer",
        "Vikram Patil",
    ],
    "Credit_Score": [720, 650, 780, 610, 810],
    "Annual_Income": [60000, 45000, 90000, 38000, 120000],
    "Debt_Ratio": [0.30, 0.55, 0.20, 0.60, 0.15],
    "Default_Status": [1, 0, 1, 0, 1],  # 1 = Low Risk, 0 = High Risk
}

df = pd.DataFrame(data)
df.to_excel("financial_ml_inputs.xlsx", index=False)
print("Successfully generated 'financial_ml_inputs.xlsx' for ML and Traditional scripts.")
