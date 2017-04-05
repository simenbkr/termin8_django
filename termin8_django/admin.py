from django.contrib import admin

from termin8_django.models import *
# Register your models here.

admin.site.register(Plant)
admin.site.register(Room)
admin.site.register(PlantType)
admin.site.register(SensorHistory)
admin.site.register(WateringHistory)
admin.site.register(UserOwnsPlant)