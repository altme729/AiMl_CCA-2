# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shlok Shirke]
# Admin PRN: [1302250028]
# File 3: Hugging Face Sentiment Monitor (Expanded Problem Statements)
# ==============================================================================
from transformers import pipeline


def run_sentiment_monitor():
  print("Initializing Hugging Face Sentiment Analysis Pipeline...")
  # Using a lightweight pre-trained sentiment analysis model
  sentiment_pipeline = pipeline(
      "sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
  )

  # Custom Problem Statements / Test Cases
  problem_statements = [
      (
          "Problem 1 (FinTech App UI): The new UPI payment gateway update is"
          " extremely smooth and fast!"
      ),
      (
          "Problem 2 (Customer Support): I have been locked out of my digital"
          " wallet account for 3 days with zero support response."
      ),
      (
          "Problem 3 (E-Commerce Decor): The handcrafted concrete coaster and"
          " moon lamp arrived safely and look stunning on my desk."
      ),
      (
          "Problem 4 (Loan Processing): The automated loan disbursal took less"
          " than 10 minutes, highly efficient service."
      ),
      (
          "Problem 5 (Billing Issue): Unexpected hidden transaction charges"
          " were deducted from my savings account."
      ),
  ]

  print("\n--- Sentiment Analysis Results ---")
  for statement, text in [(p[0], p[1]) for p in enumerate(problem_statements, 1)]:
    result = sentiment_pipeline(text)[0]
    print(f"\nContext: {statement}")
    print(f"Text: '{text}'")
    print(
        f"Sentiment: {result['label']} (Confidence:"
        f" {result['score']:.4f})"
    )


if __name__ == "__main__":
  run_sentiment_monitor()
