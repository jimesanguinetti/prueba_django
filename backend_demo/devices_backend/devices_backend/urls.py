from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path
from api.routers import app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', app.urls)
]