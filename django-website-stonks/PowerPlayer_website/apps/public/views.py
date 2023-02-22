from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.cache import cache
from django.utils import timezone
import random
import atexit


def five():
    return 6


def index(request):
    # Get the random number from the cache, or generate a new one if it doesn't exist
    random_number = cache.get('random_number')
    random_number_time = cache.get('random_number_time')
    if random_number is None or random_number_time is None or random_number_time < timezone.now() - timezone.timedelta(minutes=2):
        random_number = five()
        random_number_time = timezone.now()
        cache.set('random_number', random_number)
        cache.set('random_number_time', random_number_time)

    context = {'random_number': random_number}
    return render(request, 'index.html', context)

def random_number(request):
    # Get the random number from the cache, or generate a new one if it doesn't exist
    random_number = cache.get('random_number')
    random_number_time = cache.get('random_number_time')
    if random_number is None or random_number_time is None or random_number_time < timezone.now() - timezone.timedelta(minutes=2):
        random_number = random.randint(1, 5)
        random_number_time = timezone.now()
        cache.set('random_number', random_number)
        cache.set('random_number_time', random_number_time)

    data = {'random_number': random_number}
    return JsonResponse(data)

def leaderboards(request: HttpRequest) -> HttpResponse:
    return render(request, 'leaderboards.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')

def shutdown():
    pass

cache.clear()
atexit.register(shutdown)
