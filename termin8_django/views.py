from django.contrib.auth.models import User, Group
from rest_framework import viewsets
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


class PlantTypeViewSet(viewsets.ModelViewSet):
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeSerializser


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


def logout_user(request):
    logout(request)
    return HttpResponse(str("Logged out"))
