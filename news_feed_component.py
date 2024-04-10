from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from google_news_feed import GoogleNewsFeed
import nest_asyncio

nest_asyncio.apply()

class NewsFeedComponent:
    def __init__(self):
        self.gnf = GoogleNewsFeed(language='en',country='US')

    def query(self, tag: str):
        return self.gnf.query(tag)