from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Users, Protocols, Objects, Defects
import json

# Create your views here.
def protocolsView(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login")
    
    data = getProtocols(request.user)
    return render(request, 'protocols.html', {"res": data})

def deleteProtocol(request):
    id = request.GET.get('id')
    Users.disableProtocol(request.user, id)
    return HttpResponse("OK!")

def getProtocols(user):
    protocols = Protocols.objects.filter(user=user).exclude(active=0).values()
    return protocols
