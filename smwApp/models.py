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

@receiver(pre_save, sender=Door)
def track_state_change(sender, instance, **kwargs):
    if instance.pk:
        door = Door.objects.get(pk=instance.pk)
        previous_state = door.state
        door.last_online = timezone.now()
        if previous_state != instance.state:
            DoorStateChange.objects.create(state=instance.state)
