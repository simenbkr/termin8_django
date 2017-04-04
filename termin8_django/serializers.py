from django.contrib.auth.models import User, Group
from rest_framework import serializers
from termin8_django.models import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PlantSerializer(ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'