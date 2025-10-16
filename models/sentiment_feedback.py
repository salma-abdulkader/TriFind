from transformers import pipeline

# Sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Save user feedback
def submit_feedback_fn(feedback_text):
    if not feedback_text.strip():
        return "⚠️ Please write feedback before submitting."

    result = sentiment_analyzer(feedback_text)[0]
    sentiment = result["label"]
    score = result["score"]

    with open("data/user_feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"{feedback_text} | Sentiment: {sentiment} ({score:.2f})\n")

    return f"✅ Thanks for your feedback! Sentiment detected: {sentiment} ({score:.2f})"
