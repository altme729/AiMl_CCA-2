# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shlok Shirke]
# Admin PRN: [1302250028]
# File 1: Traditional Programming Vs Machine Learning Programming Code
# ==============================================================================
import openpyxl
from sklearn.linear_model import LogisticRegression
import pandas as pd


def traditional_credit_assessment(file_path):
  """Traditional Programming: Hardcoded rule-based logic to approve/reject loans."""
  print("--- Running Traditional Rule-Based Programming ---")
  wb = openpyxl.load_workbook(file_path)
  sheet = wb.active

  results = []
  for row in sheet.iter_rows(min_row=2, values_only=True):
    name, credit_score, income, debt_ratio, default_status = row
    # Hardcoded business rules
    if credit_score >= 700 and income >= 50000 and debt_ratio < 0.4:
      decision = "Approved"
    else:
      decision = "Rejected"
    results.append(
        f"Customer: {name} | Score: {credit_score} | Decision: {decision}"
    )

  return results


def machine_learning_credit_assessment(file_path):
  """Machine Learning Programming: Data-driven predictive modeling."""
  print("\n--- Running Machine Learning Programming ---")
  df = pd.read_excel(file_path)

  # Features and Target
  X = df[["Credit_Score", "Annual_Income", "Debt_Ratio"]]
  y = df["Default_Status"]  # 1 for safe, 0 for risky

  # Train a simple Logistic Regression model
  model = LogisticRegression()
  model.fit(X, y)

  predictions = model.predict(X)
  df["ML_Prediction"] = [
      "Approved" if p == 1 else "Rejected" for p in predictions
  ]

  return df[["Customer_Name", "ML_Prediction"]]


if __name__ == "__main__":
  excel_file = "financial_ml_inputs.xlsx"

  # Execute Traditional approach
  trad_results = traditional_credit_assessment(excel_file)
  for res in trad_results:
    print(res)

  # Execute ML approach
  ml_results = machine_learning_credit_assessment(excel_file)
  print("\nML Model Results:")
  print(ml_results)
