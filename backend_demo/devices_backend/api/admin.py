from django.contrib import admin
from api.models import Location, Device

# Register your models here.

admin.site.register(Device) 
admin.site.register(Location)