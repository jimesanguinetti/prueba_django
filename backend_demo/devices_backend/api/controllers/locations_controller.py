from django.shortcuts import get_object_or_404
from ninja import Router
from api.models import Location
from ..schemas.location_schemas import (
    LocationSchema
)

location_app = Router()

@location_app.get("/", response=list[LocationSchema])
def get_devices(request):
    return Location.objects.all()