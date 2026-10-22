# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Anshika Sakhuja]
# Admin PRN: [1302250237]
# File 3: Hugging Face Sentiment Monitor (Expanded Problem Statements)
# ==============================================================================

import pandas as pd
from transformers import pipeline

def analyze_and_export_sentiments():
    print("--- Loading Hugging Face Sentiment Analysis Pipeline ---")
    # Load default sentiment analysis pipeline (DistilBERT)
    sentiment_pipeline = pipeline("sentiment-analysis")

    # The original dataset provided by the admin
    problem_statements = [
        "The automated loan approval process was remarkably swift and transparent.",
        "I was charged unauthorized micro-transaction fees on my mobile wallet.",
        "The stock market performance remained flat throughout the trading session.",
        "Customer service completely failed to rectify my blocked payment transfer.",
        "This new cross-border payment integration dramatically cuts down wire transfer fees.",
        "The mobile banking app keeps crashing every time I try to check my account balance."
    ]

    results_data = []

    print("\n--- Processing Problem Statements ---")
    for statement in problem_statements:
        result = sentiment_pipeline(statement)[0]
        
        # Store the results in a dictionary instead of just printing them
        results_data.append({
            "Statement": statement,
            "Sentiment": result['label'],
            "Confidence_Score": round(result['score'], 4)
        })
        
    # Convert the processed data into a Pandas DataFrame
    df = pd.DataFrame(results_data)
    
    # Save the analyzed data for reporting/auditing
    output_filename = "sentiment_analysis_report.csv"
    df.to_csv(output_filename, index=False)
    
    print(f"Analysis complete! Results successfully saved to '{output_filename}'")
    
    # Generate a quick summary of the findings
    print("\n--- Sentiment Summary ---")
    summary = df['Sentiment'].value_counts().to_string()
    print(summary)

if __name__ == "__main__":
    analyze_and_export_sentiments()
