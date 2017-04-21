from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User, Group
from termin8_django.models import *
from rest_framework import viewsets, generics
from serializers import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


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
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = PlantSerializer

    def get_queryset(self):
        """
        Only return the Plants the current
        user is an owner of. 
        """
        user = self.request.user
        return Plant.objects.filter(owned_by=user)

    def perform_create(self, serializer):
        property = serializer.save(owned_by=self.request.user)

class RoomViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SensorHistoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = SensorHistorySerializer

    def get_queryset(self):
        """
        Only return sensor data
        about plants owned by user
        """
        user = self.request.user
        return SensorHistory.objects.filter(plant__owned_by=user)


class WateringHistoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = WateringHistorySerializer

    def get_queryset(self):
        """"
        Only return watering data
        about plants owned by user
        """
        user = self.request.user
        return WateringHistory.objects.filter(plant__owned_by=user)


class PlantTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeSerializer


@require_http_methods(['POST'])
@csrf_exempt
@login_required
def water_plant(request):

    plant_id = request.POST.get('plant')
    if not plant_id: return HttpResponse(str('You did not provide a plant id!'))

    plant = Plant.get_by_id(Plant, plant_id)
    if not plant:
        return HttpResponse(str('No plants with that id!'))

    user = request.user
    if not (plant.owned_by_user(user)):
        return HttpResponse(str('You dont own that plant!'))

#    We gucchi, now lets post to the MQTT-broker.
    import paho.mqtt.client as mqtt
    client = mqtt.Client()
    client.username_pw_set('termin8', 'jeghaterbarnmedraraksent')
    client.connect('termin8.tech', 8883,300)

#    the_time = request.POST.get('time')
    the_time = 1
    topic = 'controller/{}'.format(plant_id)
    payload = 'time:{}'.format(the_time)

    client.publish(topic, payload)

    return HttpResponse(str('Started watering plant with id {} for {}s'.format(plant_id, the_time)))


@csrf_exempt
def show_page(request):
    return render(request, 'index.html', {})



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
