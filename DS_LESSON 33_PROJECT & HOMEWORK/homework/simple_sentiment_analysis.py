from textblob import TextBlob

# Sample text data
text_data = [
    "I love this movie, it's amazing!",
    "The food at that restaurant was terrible.",
    "The weather today is beautiful.",
    "I feel so happy right now.",
    "This book is boring.",
    "The service was excellent!"
]

# Function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Main loop
for text in text_data:
    sentiment = analyze_sentiment(text)
    print(f"Text: {text} \nSentiment: {sentiment}\n")
