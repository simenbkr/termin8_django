from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models


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

class SensorHistory(models.Model):
    plant_id = models.ForeignKey(Plant)
    temp = models.FloatField()
    moisture = models.FloatField()

class WateringHistory(models.Model):
    plant_id = models.ForeignKey(Plant)
    temp = models.FloatField()
    moisture = models.FloatField()
    time_watered = models.TimeField()

class AppUser(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=512)

class UserOwnsPlant(models.Model):
    plant_id = models.ForeignKey(Plant)
    user_id = models.ForeignKey(AppUser)
