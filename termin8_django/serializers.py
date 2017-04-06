from django.contrib.auth.models import User, Group
from rest_framework import serializers
from termin8_django.models import *
from rest_framework.serializers import ModelSerializer

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserPlantSerializer(ModelSerializer):
    class Meta:
        model = UserOwnsPlant
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class PlantTypeSerializser(ModelSerializer):

    class Meta:
        model = PlantType
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
    owned_by = UserSerializer(read_only=True, many=True)
    sensor_data = serializers.SerializerMethodField()
    watering_history = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = ('id', 'name', 'room', 'sensor_data','watering_history', 'owned_by')

    def get_sensor_data(self, obj):
        return {'temp': obj.get_sensor_history()[-1].get_temp(), 'moisture': obj.get_sensor_history()[-1].get_moisture()}

    def get_watering_history(self, obj):
        return {'temp': obj.get_watering_history()[-1].get_temp(), 'moisture': obj.get_watering_history()[-1].get_moisture()}
