# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shravan Sagale]
# Admin PRN: [1302250620]
# File 3: Hugging Face Sentiment Monitor (Expanded Problem Statements)
# ==============================================================================

from transformers import pipeline

def run_sentiment_monitor():
    print("--- Loading Hugging Face Sentiment Analysis Pipeline ---")
    # Load default sentiment analysis pipeline (DistilBERT)
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Expanded list of financial and fintech problem statements
    problem_statements = [
        "The automated loan approval process was remarkably swift and transparent.",
        "I was charged unauthorized micro-transaction fees on my mobile wallet.",
        "The stock market performance remained flat throughout the trading session.",
        "Customer service completely failed to rectify my blocked payment transfer.",
        "This new cross-border payment integration dramatically cuts down wire transfer fees.",
        "The mobile banking app keeps crashing every time I try to check my account balance."
    ]

    print("\n--- Processing Problem Statements ---")
    for idx, statement in enumerate(problem_statements, start=1):
        result = sentiment_pipeline(statement)[0]
        label = result['label']
        score = result['score']
        
        print(f"\n[Problem Statement {idx}]: \"{statement}\"")
        print(f" Predicted Sentiment: {label} | Confidence: {score:.4f}")

if __name__ == "__main__":
    run_sentiment_monitor()
