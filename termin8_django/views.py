from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SensorHistoryViewSet(viewsets.ModelViewSet):
    queryset = SensorHistory.objects.all()
    serializer_class = SensorHistorySerializer

class WateringHistoryViewSet(viewsets.ModelViewSet):
    queryset = WateringHistory.objects.all()
    serializer_class = WateringHistorySerializer