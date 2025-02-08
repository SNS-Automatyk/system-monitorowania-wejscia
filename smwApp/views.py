from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    door = Door.objects.first()
    online = door.last_online and door.last_online >= timezone.now() - timezone.timedelta(minutes=2)
    last_change = DoorStateChange.objects.order_by('timestamp').last().timestamp
    locked = door.state == 'locked'
    return render(request, 'home.html', {'online': online, 'locked': locked, 'last_change': last_change})


# filepath: /Users/marvin/Programowanie/sns-automatyk/system-monitorowania-wejscia/smwApp/views.py
from rest_framework import viewsets, mixins
from .models import Door
from .serializers import DoorSerializer

class DoorViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer