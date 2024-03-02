from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.exchange_rate, name='exchange-rate'),
]