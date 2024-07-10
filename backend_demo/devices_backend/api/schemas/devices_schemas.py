from ninja import ModelSchema, Schema
from api.models import Device
from .location_schemas import LocationSchema

# schemas provide validation of the structure of the data, and also provides documentation for the endpoint

class DeviceSchema(ModelSchema):
    location: LocationSchema | None = None

    class Meta:
        model = Device
        fields = ('id', 'name', 'slug', 'location', 'image', 'thumbnail')

# to create a new device, a different schema es needed 
class DeviceCreateSchema(Schema):
    name: str
    location_id: int | None = None
    image: str
    thumbnail: str 

class DeviceUpdateSchema(Schema):
    lname: str
    image: str
    thumbnail: str 

class Error(Schema):
    message: str

class DeviceLocationPatch(Schema):
    location_id: int | None = None

    