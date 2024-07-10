from ninja import ModelSchema, Schema
from api.models import Location

# schemas provide validation of the structure of the data, and also provides documentation for the endpoint

class LocationSchema(ModelSchema):
    class Meta: 
        model = Location
        fields = ('id', 'name')
