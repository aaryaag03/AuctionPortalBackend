from unittest.util import _MAX_LENGTH
from django.db import models

class Users(models.Model):
  username = models.CharField(max_length=255)
  role = models.BooleanField()
  password = models.CharField(max_length=500)
  email = models.CharField(max_length=50)
  balance = models.IntegerField()


class Items_on_bid(models.Model):
  item_name=models.CharField(max_length=255)
  item_descr=models.CharField(max_length=255)
  item_picture=models.CharField(max_length=255)
  minimum_bid=models.IntegerField()
  highest_bid=models.IntegerField()
  highest_bidder_username=models.CharField(max_length=255)
  owner_username=models.CharField(max_length=255)
  valid=models.BooleanField()


class Items_claimed(models.Model):
  item_name=models.CharField(max_length=255)
  item_descr=models.CharField(max_length=255)
  item_picture=models.CharField(max_length=255)
  owner_username=models.CharField(max_length=255)
