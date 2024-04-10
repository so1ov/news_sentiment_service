from aiohttp import web
import news_hub_service

service = news_hub_service.NewsHubService()
web.run_app(service.app)