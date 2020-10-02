from django.urls import path
from protocols import views

urlpatterns = [
    path('', views.protocolsView, name='protocolsView'),
    path('deleteprotocol', views.deleteProtocol, name='deleteProtocol')
]