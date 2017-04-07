from django.contrib.auth.models import User, Group
from termin8_django.models import *
from rest_framework import viewsets, generics
from serializers import *
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


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


class PlantViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    serializer_class = PlantSerializer

    def get_queryset(self):
        """
        Only return the Plants the current
        user is an owner of. 
        """
        user = self.request.user
        return Plant.objects.filter(owned_by=user)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SensorHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = SensorHistorySerializer

    def get_queryset(self):
        """
        Only return sensor data
        about plants owned by user
        """
        user = self.request.user
        return SensorHistory.objects.filter(plant__owned_by=user)


class WateringHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = WateringHistorySerializer

    def get_queryset(self):
        """"
        Only return watering data
        about plants owned by user
        """
        user = self.request.user
        return WateringHistory.objects.filter(plant__owned_by=user)


class PlantTypeViewSet(viewsets.ModelViewSet):
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeSerializer


@csrf_exempt
def login_template(request):
    return render(request, 'accounts/login.html', {})


@csrf_exempt
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(str("Success"))
    return HttpResponse(str("Failure"))

@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponse(str("Logged out"))
