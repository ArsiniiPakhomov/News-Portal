from datetime import timedelta
import datetime
from celery import shared_task
from django.dispatch import receiver
from .models import Post, PostCategory, Category
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone

@shared_task
def notification_every_week():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_in__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email= settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def send_notification(pk):
    post =Post.objects.get(pk=pk)
    title = post.title
    preview = post.preview()
    categories = post.category.all()
    subscribers_emails = []

    for cat in categories:
        subscribers = cat.subscribers.all()
        subscribers_emails += [s.email for s in subscribers]
    
    subscribers_emails = set(subscribers_emails)
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/posts/post/{pk}'
        }

    )

    msg = EmailMultiAlternatives(
        subject= title,
        body='',
        from_email= settings.DEFAULT_FROM_EMAIL,
        to = subscribers_emails
        )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()




    

