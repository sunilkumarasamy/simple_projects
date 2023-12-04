import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Welcome to the Sentiment Analysis Tool!")
    user_text = input("Enter the text you want to analyze: ")

    sentiment = analyze_sentiment(user_text)
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()

