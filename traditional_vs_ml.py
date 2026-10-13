# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Anshika Sahuja]
# Admin PRN: [1302250237]
# File 1: Traditional Programming Vs Machine Learning Programming Code
# ==============================================================================

import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    print("--- 1. Reading Input Data from Excel File ---")
    excel_filename = "ml_input_data.xlsx"
    
    try:
        df = pd.read_excel(excel_filename)
    except FileNotFoundError:
        print(f"Error: '{excel_filename}' not found! Ensure the file exists in the directory.")
        return

    # --------------------------------------------------------------------------
    # APPROACH 1: Traditional Programming (Hardcoded Business Logic)
    # --------------------------------------------------------------------------
    def traditional_risk_classifier(credit_score, income_k):
        if credit_score < 650 or income_k < 45:
            return "High Risk"
        else:
            return "Low Risk"

    df['Traditional_Prediction'] = df.apply(
        lambda row: traditional_risk_classifier(row['Credit_Score'], row['Income_k']), axis=1
    )

    # --------------------------------------------------------------------------
    # APPROACH 2: Machine Learning Programming
    # --------------------------------------------------------------------------
    X = df[['Credit_Score', 'Income_k']]
    y = df['Actual_Risk']

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    df['ML_Prediction'] = model.predict(X)

    print("\n--- 2. Results Comparison ---")
    comparison = df[['Customer_ID', 'Actual_Risk', 'Traditional_Prediction', 'ML_Prediction']]
    print(comparison.to_string(index=False))

    # --------------------------------------------------------------------------
    # COLLABORATOR ADDITION: Evaluation & Model Persistence
    # --------------------------------------------------------------------------
    print("\n--- 3. Performance Evaluation ---")
    
    # Calculate accuracy for both approaches
    trad_acc = accuracy_score(df['Actual_Risk'], df['Traditional_Prediction'])
    ml_acc = accuracy_score(df['Actual_Risk'], df['ML_Prediction'])
    
    print(f"Traditional Rule Accuracy: {trad_acc * 100:.2f}%")
    print(f"Machine Learning Accuracy:   {ml_acc * 100:.2f}%")
    
    print("\nMachine Learning Classification Report:")
    print(classification_report(df['Actual_Risk'], df['ML_Prediction'], zero_division=0))

    print("--- 4. Saving the ML Model ---")
    model_filename = "loan_risk_model.joblib"
    joblib.dump(model, model_filename)
    print(f"Model successfully saved to '{model_filename}' for production use.")

if __name__ == "__main__":
    main()
