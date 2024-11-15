from django.urls import path
from .views import (NewsList, NewDatail,Search, NewCreat, ArtCreat)

urlpatterns = [
    path ('', NewsList.as_view()),
    path('<int:pk>',NewDatail.as_view()),
    path('search',Search.as_view()),
    path('create/', NewCreat.as_view()),
    path('create/articles', ArtCreat.as_view()),
]


