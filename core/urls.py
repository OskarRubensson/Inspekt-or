from django.urls import path
from . import views

urlpatterns = [
    path('', include('home.urls')),
]