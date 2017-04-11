from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from time import time
from termin8_django.models import *
from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication

"""
class AppUser(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=512)

    def __unicode__(self):
        return self.email
    def __str__(self):
        return self.__unicode__()
"""


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.__unicode__()


class PlantType(models.Model):
    name = models.CharField(max_length=100)
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    min_moisture = models.FloatField()
    max_moisture = models.FloatField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Plant(models.Model):
    name = models.CharField(max_length=45)
#    max_temp = models.FloatField()
#    min_temp = models.FloatField()
#    min_moisture = models.FloatField()
#    max_moisture = models.FloatField()
    last_watered = models.TimeField(null=True)
    automatic_water = models.BooleanField()
    room = models.ForeignKey(Room)
    plant_type = models.ForeignKey(PlantType)
    owned_by = models.ManyToManyField(User)

    def get_watering_history(self):
        return list(WateringHistory.objects.filter(plant=self))

    def get_sensor_history(self):
        return list(SensorHistory.objects.filter(plant=self))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class SensorHistory(models.Model):
    plant = models.ForeignKey(Plant)
    temp = models.FloatField()
    moisture = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.timestamp

    def __str__(self):
        return self.__unicode__()

    def get_temp(self):
        return self.temp

    def get_moisture(self):
        return self.moisture

    def get_timestamp(self):
        return self.timestamp


class WateringHistory(models.Model):
    plant = models.ForeignKey(Plant)
    temp = models.FloatField()
    moisture = models.FloatField()
    time_watered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.time_watered.__str__()

    def get_temp(self):
        return self.temp

    def get_moisture(self):
        return self.moisture

    def get_timestamp(self):
        return self.time_watered

    def is_owner(self, user):
        if user == self.plant.owned_by:
            return True
        return False


class UserOwnsPlant(models.Model):
    plant = models.ForeignKey(Plant)
    user = models.ForeignKey(User)
