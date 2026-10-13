# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Aryan]
# Admin PRN: [1302250491]
# File 2: Generates 'ml_input_data.xlsx'
# ==============================================================================

import pandas as pd

# Credit score and Income (in thousands) data for loan risk classification
dataset = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Credit_Score': [720, 580, 680, 800],
    'Income_k': [65, 30, 50, 40, 90, 25, 48, 110],
    'Actual_Risk': ['Low Risk', 'High Risk', 'Low Risk', 'High Risk', 'Low Risk', 'High Risk', 'Low Risk', 'Low Risk']
}

df = pd.DataFrame(dataset)

# Save to Excel format
output_filename = "ml_input_data.xlsx"
df.to_excel(output_filename, index=False)
print(f"File '{output_filename}' created successfully!")
