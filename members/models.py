from unittest.util import _MAX_LENGTH
from django.db import models

class Users(models.Model):
  username = models.CharField(max_length=255)
  role = models.BooleanField()
  password = models.CharField(max_length=500)
  email = models.CharField(max_length=50)
  balance = models.IntegerField()