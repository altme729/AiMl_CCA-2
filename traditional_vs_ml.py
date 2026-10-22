# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Yukta Kulkarni]
# Admin PRN: [1302250198]
# File 1: Traditional Programming Vs Machine Learning Programming Code
# ==============================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def traditional_fraud_check(file_path):
    """Traditional logic using hardcoded thresholds."""
    print("--- Traditional Rule-Based Fraud Detection ---")
    df = pd.read_excel(file_path)
    results = []
    
    for index, row in df.iterrows():
        # Rule: If transaction is > 50,000 AND is international AND has failed attempts
        if row['Amount_INR'] > 50000 and row['Is_International'] == 1 and row['Failed_Attempts'] >= 2:
            status = "Flagged: Fraud"
        else:
            status = "Clear"
        results.append(f"Txn ID {row['Txn_ID']}: {status}")
        
    return results

def ml_fraud_check(file_path):
    """Machine Learning logic using a Decision Tree Classifier."""
    print("\n--- Machine Learning Fraud Detection ---")
    df = pd.read_excel(file_path)
    
    # Features (X) and Target (y)
    X = df[['Amount_INR', 'Is_International', 'Failed_Attempts']]
    y = df['Is_Fraud']
    
    # Train Decision Tree Model
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X, y)
    
    # Predict
    predictions = clf.predict(X)
    df['ML_Status'] = ["Flagged" if p == 1 else "Clear" for p in predictions]
    
    return df[['Txn_ID', 'ML_Status']]

if __name__ == "__main__":
    input_file = "fraud_detection_inputs.xlsx"
    
    # Run Traditional
    trad_out = traditional_fraud_check(input_file)
    for res in trad_out:
        print(res)
        
    # Run ML
    ml_out = ml_fraud_check(input_file)
    print("\nML Predictions:\n", ml_out.to_string(index=False))
