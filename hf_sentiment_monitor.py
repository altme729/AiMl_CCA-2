# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shravan Sagale]
# Admin PRN: [1302250620]
# File 3: Hugging Face Sentiment Monitor (Expanded Problem Statements)
# ==============================================================================

from transformers import pipeline

def run_advanced_sentiment_monitor():
    print("Loading Hugging Face Pipeline...")
    # Using a different model optimized for varied text
    analyzer = pipeline("sentiment-analysis")
    
    # New problem statements encompassing finance, tax, and decor e-commerce
    problem_statements = {
        "Trading App Crash": "The equity analysis dashboard crashed right during market hours, causing me huge losses.",
        "Taxation Software": "Filing my direct taxes was surprisingly easy and the interface is very intuitive.",
        "Mutual Fund Returns": "The SIP mutual fund returns are average, neither great nor terrible.",
        "E-Commerce Decor": "The lotus-shaped incense holder and crescent moon mirror I ordered arrived broken. Terrible packaging.",
        "FinTech UI Update": "I love the new dark mode and fast UPI integrations in the latest update!"
    }
    
    print("\n--- Sentiment Analysis Output ---")
    for category, text in problem_statements.items():
        result = analyzer(text)[0]
        print(f"[{category}]")
        print(f"Review: {text}")
        print(f"Sentiment: {result['label']} | Score: {result['score']:.2f}\n")

if __name__ == "__main__":
    run_advanced_sentiment_monitor()
