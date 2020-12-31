from django.db import models
from accounts.models import User
import json

# Create your models here.
class Users(models.Model):

    def __str__(self):
        return "%s %s" % (self.first, self.last)
    
    def getProtocols(self, user):
        protocols = Protocols.objects.filter(user=user).exclude(active=0).values()
        return protocols
    
    def getProtocol(user, pid):
        
        jsonstring = '{"user":"' + user.email + '",'
        protocol = user.protocols_set.get(id=pid)

        jsonstring += '"name":"' + protocol.name + '",' 
        jsonstring += '"id":"' + str(protocol.id) + '",' 
        jsonstring += '"date":"' + protocol.date.strftime("%Y-%m-%d") + '",'
        jsonstring += '"location":"' + protocol.location + '",' 
        jsonstring += '"objects":[ '
        
        for objects in protocol.objects_set.all():

            jsonstring += '{"name":"' + objects.name + '",'
            jsonstring += '"id":"' + str(objects.id) + '",'
            jsonstring += '"defects":[ '
            for defects in objects.defects_set.all():
                jsonstring += '{"name":"' + defects.name + '",'
                jsonstring += '"id":"' + str(defects.id) + '",'
                jsonstring += '"severity":"' + defects.severity.upper() + '",'
                jsonstring += '"description":"' + defects.description + '"},'
            jsonstring = jsonstring[:-1]
            jsonstring += ']},'
        jsonstring = jsonstring[:-1]
        jsonstring += "]}"
        result = json.loads(json.dumps(jsonstring))
        return result
    
    def disableProtocol(user, pid):
        protocol = Protocols.objects.get(id=pid)
        protocol.active = 0
        protocol.save()

        return


class Protocols(models.Model):
    location = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Objects(models.Model):
    name = models.CharField(max_length=30)
    protocol_id = models.ForeignKey(Protocols, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Defects(models.Model):
    name = models.CharField(max_length=30)
    severity = models.CharField(max_length=1)
    description = models.CharField(max_length=255)
    object_id = models.ForeignKey(Objects, on_delete=models.CASCADE)

    def __str__(self):
        return self.name