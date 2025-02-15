from django.db import models
from django.contrib.auth.models import User
# from news.models import *
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = Post.objects.filter(author=self).aggregate(pr= Coalesce(Sum('rating'),0))['pr']
        comments_rating = Comment.objects.filter(user = self.user).aggregate(cr = Coalesce(Sum('rating'), 0))['cr']
        posts_comments_rating = Comment.objects.filter(post__author=self).aggregate(pcr = Coalesce(Sum('rating'),0))['pcr']
        # posts = Post.objects.filter(author=self)
        # for p in posts:
        #     posts_rating +=p.rating
        # comments = Comment.objects.filter(user = self.user)
        # for c in comments:
        #     comments_rating +=c.rating
        # posts_comments = Comment.objects.filter(post__author=self)
        # for pc in posts_comments:
        #     posts_comments_rating += pc.rating

        # print(posts_rating)
        # print("................")
        # print(comments_rating)
        # print("................")
        # print(posts_comments_rating)
        
        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()
    
    def __str__(self):
        return self.user.username




class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')
    
    
    def __str__(self):
        return self.name

class Post(models.Model):

    news = "NW"
    articles = "AR"

    POST_TYPE = [
        (news, "Новость"),
        (articles, "Статья")
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPE, default=news)
    date_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()
    
    def preview(self, length=124):
        return f"{self.text[:length]}..." if len(self.text) > length else self.text
    
    def __str__(self):
        return self.title.title()
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_in = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()
    

        

