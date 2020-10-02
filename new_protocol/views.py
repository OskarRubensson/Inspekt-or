from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from core.models import Users, Protocols, Objects, Defects

# Create your views here.
def newView(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login")

    id = request.GET.get('id', '0')
    if id == 0 or id == '0':
        res = {
            "user": request.user
        }
    else: 
        res = json.loads(Users.objects.get(id=1).getProtocol(request.user, id))
    return render(request, 'new_protocol.html', {"res": res, "pid": id})

def editView(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login")

    id = request.GET.get('id', '0')
    result = json.loads(Users.getProtocol(request.user, id))
    return render(request, 'new_protocol.html', {"res": result})

def submitProtocol(request):
    p = json.loads(request.GET.get('protocol', ''))
    old_pid = request.GET.get('old_pid', '0')

    if old_pid != '0' and old_pid != 0:
        Users.disableProtocol(request.user, request.user, old_pid)
    
    if request.user != 0:
        protocol = Protocols(name=p['name'], location=p['location'], date=p['date'], user=request.user)
        protocol.save()
        for o in p['objects']:
            obj = Objects(name=o['name'], protocol_id=protocol)
            obj.save()
            for d in o['defects']:
                defect = Defects(name=d['name'], severity=d['severity'], description=d['description'], object_id=obj)
                defect.save()

        return HttpResponse('Success!')
    else:
        return HttpResponse('Error!')