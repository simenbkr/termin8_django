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


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class SensorHistorySerializer(ModelSerializer):
    plant_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = SensorHistory
        fields = ('id', 'temp', 'moisture', 'timestamp', 'plant_id')


class WateringHistorySerializer(ModelSerializer):
    plant_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = WateringHistory
        fields = '__all__'


class PlantSerializer(ModelSerializer):
    sensor_data = serializers.SerializerMethodField()
    watering_history = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = ('id', 'name', 'room', 'sensor_data','watering_history')

    def get_sensor_data(self, obj):
        return {'temp': obj.get_sensor_history()[-1].get_temp(), 'moisture': obj.get_sensor_history()[-1].get_moisture()}

    def get_watering_history(self, obj):
        return {'temp': obj.get_watering_history()[-1].get_temp(), 'moisture': obj.get_watering_history()[-1].get_moisture()}
