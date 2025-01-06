# from celery import shared_task
# from django.dispatch import receiver
# from .models import Post, PostCategory
# from django.core.mail import send_mail, EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.conf import settings
# from django.utils import timezone

# @shared_task
# def send_notification(preview, pk, titel, subscribers):
#     html_content = render_to_string(
#         'tempaltes/post_created_email.html',{
#             'text': preview,
#             'link': f'{settings.SITE_URL}/posts/{pk}'
#         }
#     )

#     msg = EmailMultiAlternatives(
#         subject=titel,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#     )
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


