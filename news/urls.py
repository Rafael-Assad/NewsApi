from django.urls import path
from .views import listNews

urlpatterns = [
    path('', listNews),
]