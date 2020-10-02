from django.urls import path
from new_protocol import views

urlpatterns = [
    path('', views.newView, name='newView'),
    path('submitprotocol/', views.submitProtocol, name="submitprotocol")
]