# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shravan Sagale]
# Admin PRN: [1302250620]
# File 1: Traditional Programming Vs Machine Learning Programming Code
# ==============================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def main():
    print("--- 1. Reading Input Data from Excel File ---")
    excel_filename = "ml_input_data.xlsx"
    
    try:
        df = pd.read_excel(excel_filename)
        print("Dataset loaded successfully:")
        print(df)
    except FileNotFoundError:
        print(f"Error: '{excel_filename}' not found! Ensure the file exists in the directory.")
        return

    # --------------------------------------------------------------------------
    # APPROACH 1: Traditional Programming (Hardcoded Business Logic)
    # --------------------------------------------------------------------------
    def traditional_risk_classifier(credit_score, income_k):
        # Explicit rule: High risk if credit score < 650 OR income < 45k
        if credit_score < 650 or income_k < 45:
            return "High Risk"
        else:
            return "Low Risk"

    # Apply traditional rules
    df['Traditional_Prediction'] = df.apply(
        lambda row: traditional_risk_classifier(row['Credit_Score'], row['Income_k']), axis=1
    )

    # --------------------------------------------------------------------------
    # APPROACH 2: Machine Learning Programming (Model Training & Inference)
    # --------------------------------------------------------------------------
    # Features (Inputs) and Target (Output to Learn)
    X = df[['Credit_Score', 'Income_k']]
    y = df['Actual_Risk']

    # Initialize Decision Tree Classifier and train on existing dataset
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    # Predict using the trained model
    df['ML_Prediction'] = model.predict(X)

    # --------------------------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------------------------
    print("\n--- 2. Results Comparison ---")
    comparison = df[['Customer_ID', 'Credit_Score', 'Income_k', 'Actual_Risk', 'Traditional_Prediction', 'ML_Prediction']]
    print(comparison.to_string(index=False))

if __name__ == "__main__":
    main()
