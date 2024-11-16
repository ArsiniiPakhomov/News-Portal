from django.urls import path
from .views import (NewsList, NewDatail,Search, PostCreat, PostUpdate, PostDelete)

urlpatterns = [
    path('', NewsList.as_view(), name = "post_list"), 
    path('post/<int:pk>/',NewDatail.as_view(), name = "post_detail"),
    path('search/',Search.as_view() , name = "post_search"),
    path('news/create/', PostCreat.as_view(), name= "news_create"),
    path('articles/create/', PostCreat.as_view(), name= "articles_create"),
    path('news/update/<int:pk>/', PostUpdate.as_view(), name = "news_update"),
    path('articles/update/<int:pk>/', PostUpdate.as_view(), name = "articles_update"),
    path('news/delete/<int:pk>', PostDelete.as_view(), name = "news_delete"),
    path('articles/delete/<int:pk>', PostDelete.as_view(), name = "articlest_delete")
]


