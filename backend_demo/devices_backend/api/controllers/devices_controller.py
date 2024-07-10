from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ninja import Router, File
from ninja.files import UploadedFile
from api.models import Device, Location
from ..schemas.devices_schemas import (
    DeviceSchema,
    DeviceCreateSchema,
    Error,
    DeviceLocationPatch,
    DeviceUpdateSchema
)

device_app = Router()

@device_app.get("/", response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()


@device_app.get("/{slug}/", response=DeviceSchema)
def get_device(request, slug: str):
    device = get_object_or_404(Device, slug=slug)
    return device

@device_app.post("/", response={200: DeviceSchema, 404: Error})
def createDevice(request, device: DeviceCreateSchema):
    if device.location_id:
        location_exists = Location.objects.filter(id=device.location_id).exists()
        if not location_exists:
            return 404, {"message": "Location not found"}

    device_data = device.model_dump()
    device_model = Device.objects.create(**device_data)
    return device_model

@device_app.post('/{device_slug}/set-location/', response=DeviceSchema)
def updateDeviceLocation(request, device_slug, location: DeviceLocationPatch):
    device = get_object_or_404(Device, slug=device_slug)
    if location.location_id:
        location = get_object_or_404(Location, id=location.location_id)
        device.location = location
    else:
        device.location = None
    
    device.save()
    return device

@device_app.delete("/{slug}/", response={200: dict, 404: str})
def delete_device(request, slug: str):
    device = get_object_or_404(Device, slug=slug)
    device.delete()
    return JsonResponse({'message': 'Device deleted successfully'}, status=200)

@device_app.put("/{slug}/", response={200: DeviceSchema, 404: str})
def update_device(request, slug: str, payload: DeviceUpdateSchema):
    device = get_object_or_404(Device, slug=slug)
    
    for attr, value in payload.dict().items():
        setattr(device, attr, value)
    
    device.save()
    return device
