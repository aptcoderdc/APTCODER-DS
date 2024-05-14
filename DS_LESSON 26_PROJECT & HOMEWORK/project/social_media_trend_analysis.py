import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Sample dataset
data = {
    'Post': [
        "I love the new features of this app! #innovation",
        "This update is terrible, nothing works! #fail",
        "Best user experience ever! #UX #design",
        "I'm so frustrated with the bugs in this app. #frustration",
        "Loving the new update! #awesome #update",
    ],
    'Likes': [120, 45, 300, 50, 200]
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

# Count sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Extract hashtags
df['Hashtags'] = df['Post'].apply(lambda x: [tag.strip("#") for tag in x.split() if tag.startswith("#")])
hashtags = sum(df['Hashtags'], [])
hashtag_counts = pd.Series(hashtags).value_counts()

# Visualization
plt.figure(figsize=(14, 6))

# Plot Sentiment Analysis
plt.subplot(1, 2, 1)
sentiment_counts.plot(kind='bar', color=['green', 'grey', 'red'])
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Count')

# Plot Hashtag Trends
plt.subplot(1, 2, 2)
hashtag_counts.plot(kind='bar', color='blue')
plt.title('Hashtag Trends')
plt.xlabel('Hashtags')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# Output
print("Sentiment Analysis Counts:\n", sentiment_counts)
print("Hashtag Trends Counts:\n", hashtag_counts)
