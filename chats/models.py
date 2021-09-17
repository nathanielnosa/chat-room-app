from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=500)

  def __str__(self):
    return self.name

class Message(models.Model):
  msg = models.CharField(max_length=1000000000)
  date = models.DateTimeField(default=datetime.now, blank=True)
  user = models.CharField(max_length=500)
  room = models.CharField(max_length=500)
  
