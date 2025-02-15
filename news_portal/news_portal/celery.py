import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')
 
app = Celery('news_portal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_mondeay_8am': {
        'task': 'news.tasks.notification_every_week',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': ()
    }
}