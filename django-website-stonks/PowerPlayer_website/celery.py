from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PowerPlayer_website.settings')

app = Celery('PowerPlayer_website')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
