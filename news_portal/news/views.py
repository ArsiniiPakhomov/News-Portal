from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
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
        
class PostCreat (CreateView):
    form_class = NewsForm
    
    model = Post
   
    template_name = 'post_create.html'


    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/posts/articles/create/':
            post.post_type = 'AR'
        post.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.path == '/posts/articles/create/':
            context['post_type'] = "Статья"
        else:
            context['post_type'] = "Новость"     
        return context
         
class PostUpdate (UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'post_create.html'
    
    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     if self.request.path == '/posts/articles/update/<int:pk>/':
    #         post.post_type = 'AR'
    #     post.save()
    #     return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.path == '/posts/articles/update/<int:pk>/':
            context['post_type'] = "Редактирвоание публикации "
        else:
            context['post_type'] = "Редактирование публикации"     
        return context

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy ('post_list')

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     if self.request.path == '/posts/articles/delete/<int:pk>/':
    #         post.post_type = 'AR'
    #     post.save()
    #     return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.path == '/posts/articles/delete/<int:pk>/':
            context['post_type'] = "Удаление публикации"
        else:
            context['post_type'] = "Удаление публикации"     
        return context

    
    