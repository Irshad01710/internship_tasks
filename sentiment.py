import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

df = pd.read_csv('amazon.csv')
# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['reviewText'].apply(get_sentiment)

# Count and percentage of each sentiment
sentiment_counts = df['Sentiment'].value_counts()
total_reviews = len(df)
sentiment_percentages = (sentiment_counts / total_reviews) * 100
color_palette = {'Positive': 'green', 'Negative': 'red', 'Neutral': 'blue'}

# Plot sentiment distribution
plt.figure(figsize=(8, 6))
ax = sns.countplot(x='Sentiment', data=df, palette=color_palette)
plt.title('Sentiment Distribution')

for p in ax.patches:
    count = int(p.get_height())
    percentage = (count / total_reviews) * 100
    ax.annotate(f'{count} ({percentage:.1f}%)', (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

plt.show()
display(df[['reviewText', 'Sentiment']])

