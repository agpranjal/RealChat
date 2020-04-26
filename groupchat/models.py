from django.db import models

class Rooms(models.Model):
    room_name = models.CharField(max_length=20)
