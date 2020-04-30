from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    message_from = models.CharField(max_length=20)
    message = models.CharField(max_length=1000000)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message_from
