from django.urls import path
from . import views

from .views import random_number


app_name="public"

urlpatterns = [
    path('', views.index , name="index"),
    path('leaderboards', views.leaderboards , name="leaderboards"),
    path('contact', views.contact , name="contact"),
    path('random_number/', views.random_number, name='random_number'),
]