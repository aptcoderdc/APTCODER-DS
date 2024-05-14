import pandas as pd
from textblob import TextBlob

# Sample dataset
data = {
    'Post': [
        "Great new feature! #cool",
        "Hate the recent changes. #annoying",
        "This app is amazing! #awesome",
        "Not happy with the new update. #disappointed",
        "Fantastic user interface! #UI"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to analyze sentiment
def analyze_sentiment(post):
    analysis = TextBlob(post)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment analysis
df['Sentiment'] = df['Post'].apply(analyze_sentiment)

# Extract hashtags
df['Hashtags'] = df['Post'].apply(lambda x: [tag.strip("#") for tag in x.split() if tag.startswith("#")])
hashtags = sum(df['Hashtags'], [])
hashtag_counts = pd.Series(hashtags).value_counts()

# Output
print("Sentiment Analysis:\n", df[['Post', 'Sentiment']])
print("Hashtag Trends Counts:\n", hashtag_counts)
