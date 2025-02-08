from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class DoorStateChange(models.Model):
    STATE_CHOICES = [
        ('locked', 'Locked'),
        ('unlocked', 'Unlocked'),
    ]
    state = models.CharField(max_length=10, choices=STATE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.state} at {self.timestamp}"

class Door(models.Model):
    STATE_CHOICES = [
        ('locked', 'Locked'),
        ('unlocked', 'Unlocked'),
    ]
    state = models.CharField(max_length=10, choices=STATE_CHOICES)
    last_online = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Door is {self.state}"
    
    def save(self, *args, **kwargs):
        if self.pk:
            door = Door.objects.get(pk=self.pk)
            previous_state = door.state
            self.last_online = timezone.now()
            if previous_state != self.state:
                DoorStateChange.objects.create(state=self.state)
        super().save(*args, **kwargs)

