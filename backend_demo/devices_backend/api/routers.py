from ninja import NinjaAPI

from .controllers.devices_controller import device_app
from .controllers.locations_controller import location_app

app = NinjaAPI(version="1.0.0")

app.add_router("/devices", device_app)
app.add_router("/locations", location_app)