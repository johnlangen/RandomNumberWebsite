from celery import shared_task
from django.core.cache import cache
from PowerPlayer_website.views import generate_random_number


@shared_task
def generate_summary_task():
    summary = generate_random_number()
    cache.set('summary', summary)
