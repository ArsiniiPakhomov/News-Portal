from django.urls import path
from .views import NewsList, NewDatail

urlpatterns = [
    path ('', NewsList.as_view()),
    path('<int:pk>',NewDatail.as_view()),
]


