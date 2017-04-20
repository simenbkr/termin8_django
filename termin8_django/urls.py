"""termin8_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from termin8_django import views
from rest_framework.routers import SimpleRouter
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


router = SimpleRouter()

router.register(r'plant', views.PlantViewSet, 'Plant')
router.register(r'room', views.RoomViewSet, 'Room')
router.register(r'sensorhistory', views.SensorHistoryViewSet, 'SensorHistory')
router.register(r'wateringhistory', views.WateringHistoryViewSet, 'WateringHistory')
router.register(r'planttype', views.PlantTypeViewSet, 'PlantType')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', views.login_user, name='authenticate'),
    url(r'^login/', views.login_template, name='testing'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^water/', views.water_plant, name='waterplant'),
    url(r'^$', TemplateView.as_view(template_name='index.html'))
    #url(r'^$', views.show_page, name='react_1')
    #url(r'^.*/$', views.show_page, name='react')
]