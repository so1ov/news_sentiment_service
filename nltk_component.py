from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from google_news_feed import GoogleNewsFeed
import nest_asyncio

nest_asyncio.apply()

class NltkComponent:
    def __init__(self):
        self.gnf = GoogleNewsFeed(language='en',country='US')
        self.sid = SentimentIntensityAnalyzer()


    def sentiment(self, text) -> dict:
        sentiment = self.sid.polarity_scores(text)
        return {
            'compound': sentiment['compound'],
            'neg': sentiment['neg'],
            'neu': sentiment['neu'],
            'pos': sentiment['pos']
        }