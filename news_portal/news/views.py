from typing import Any
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView)
from .models import Post
from .filters import NewFilter
from datetime import datetime
from .forms import NewsForm


class NewsList(ListView):
    model = Post

    ordering = '-date_in'

    template_name = 'news.html'

    context_object_name = 'news'

    paginate_by = 10

    
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context ['time_now'] = datetime.utcnow()
        
        return context
        

class NewDatail(DetailView):
    model = Post

    template_name = 'new.html'

    context_object_name = 'new'

class Search(ListView):
    model = Post

    ordering = '-date_in'

    template_name = 'search.html'

    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context ['time_now'] = datetime.utcnow()
        context ['filterset'] = self.filterset
        return context
        
class NewCreat (CreateView):
    form_class = NewsForm
    
    model = Post
   
    template_name = 'new_create.html'


class ArtCreat (CreateView):
    form_class = NewsForm
    
    model = Post
   
    template_name = 'articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == 'post/create/articles':
            post.articles_news = 'AR'
        post.save
        return super().form_valid(form)
    