from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=20)
    messages = models.CharField(max_length=1000000, blank=True)

    def __str__(self):
        return self.room_name

class User(models.Model):
    username = models.CharField(max_length=20)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.username