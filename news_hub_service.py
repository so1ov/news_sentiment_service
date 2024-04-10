from aiohttp import web
from nltk_component import NltkComponent
from news_feed_component import NewsFeedComponent
from util import async_partial
from functools import partial

class NewsHubService:
    def __init__(self):
        self.app = web.Application()

        get_by_tag = async_partial(self.get_by_tag)
        self.app.add_routes([web.get('/get-by-tag', get_by_tag)])

        self.nltk_component = NltkComponent()
        self.news_feed_component = NewsFeedComponent()
    
    async def get_by_tag(self, request):
        results = self.news_feed_component.query(request.query['tag'])
        titles = [res.title for res in results]
        ret = [{'title': title, 'sentiment': self.nltk_component.sentiment(title)} for title in titles]
        return web.Response(text=str(ret))
    