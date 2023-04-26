import requests
import environ
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

BASE_DIR = environ.Path(__file__) - 2

env = environ.FileAwareEnv()
env.read_env(BASE_DIR('.env'), overwrite=True)

def get_articles_main_info(articles_list):
    filtered_articles = []

    for article in articles_list:
        new_article = {
            "author": article['author'],
            "title": article['title'],
            "description": article['description'],
        }
        filtered_articles.append(new_article)
    
    return filtered_articles

    pass

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def listNews(request):
    API_KEY = env('NEWS_API_KEY')

    news_api_url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={API_KEY}"

    news = requests.get(news_api_url).json()

    news_filtered = get_articles_main_info(news['articles'])

    return Response(news_filtered, status=status.HTTP_200_OK)