from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


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