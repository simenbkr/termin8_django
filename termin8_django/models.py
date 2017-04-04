from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from time import time

default_timestamp = datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')

class AppUser(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=512)

class Room(models.Model):
    name = models.CharField(max_length=100)


class PlantType(models.Model):
    name = models.CharField(max_length=100)

class Plant(models.Model):
    name = models.CharField(max_length=45)
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    min_moisture = models.FloatField()
    max_moisture = models.FloatField()
    last_watered = models.TimeField()
    automatic_water = models.BooleanField()
    room = models.ForeignKey(Room)
    plant_type = models.ForeignKey(PlantType)



class SensorHistory(models.Model):
    plant = models.ForeignKey(Plant)
    temp = models.FloatField()
    moisture = models.FloatField()
    timestamp = models.TimeField(default=default_timestamp)

class WateringHistory(models.Model):
    plant = models.ForeignKey(Plant)
    temp = models.FloatField()
    moisture = models.FloatField()
    time_watered = models.TimeField(default=default_timestamp)

class UserOwnsPlant(models.Model):
    plant = models.ForeignKey(Plant)
    user = models.ForeignKey(AppUser)
