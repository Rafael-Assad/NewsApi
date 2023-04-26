import requests
import environ
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

BASE_DIR = environ.Path(__file__) - 2

env = environ.FileAwareEnv()
env.read_env(BASE_DIR('.env'), overwrite=True)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def listNews(request):
    API_KEY = env('NEWS_API_KEY')

    news_api_url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={API_KEY}"

    news = requests.get(news_api_url)

    return Response(news.json(), status=status.HTTP_200_OK)