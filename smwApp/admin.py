from django.contrib import admin
from .models import Door, DoorStateChange

# Register your models here.
admin.site.register(Door)
admin.site.register(DoorStateChange)
