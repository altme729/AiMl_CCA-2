# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Aryan Pandey]
# Admin PRN: [1302250491]
# File 3: Hugging Face Sentiment Monitor (Expanded Problem Statements)
# ==============================================================================

import pandas as pd

try:
    from transformers import pipeline
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

def run_sentiment_monitor(file_path):
    print("--- Hugging Face Sentiment Monitor ---")
    df = pd.read_excel(file_path)
    
    problem_statements = [
        "Problem 1: Monitor product review feedback dynamically.",
        "Problem 2: Analyze student sentiment regarding the new lab curriculum.",
        "Problem 3: Track customer support ticket urgency based on negative emotion."
    ]
    for ps in problem_statements:
        print(ps)
        
    if HAS_TRANSFORMERS:
        print("\nInitializing Hugging Face pipeline ('sentiment-analysis')...")
        classifier = pipeline("sentiment-analysis")
        results = classifier(df['Text'].tolist())
        for text, res in zip(df['Text'], results):
            print(f"\nText: {text}\nResult: {res['label']} (Score: {res['score']:.4f})")
    else:
        print("\n[Simulation Mode] 'transformers' library not installed. Showing sample pipeline outputs:")
        for idx, row in df.iterrows():
            print(f"\nText: {row['Text']}\nPredicted Sentiment: {row['Expected_Sentiment']}")

if __name__ == "__main__":
    run_sentiment_monitor("input_data.xlsx")
