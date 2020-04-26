from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_name = models.CharField(max_length=20)
    messages = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.room_name

