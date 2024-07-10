from tkinter import Image
import uuid
from django.db import models
from django_extensions.db.fields import AutoSlugField
from io import BytesIO
from django.core.files import File

class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name') # e.g. CO2 Sensor -> co2-sensor
    location = models.ForeignKey(
        Location, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True) 

    def __str__(self):
        return f"{self.name} - {self.id}"
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url #cambiar esta url
        return ''
    
    def get_thumbnail(self):
        print("LLEGA")
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url #cambiar esta url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save() 
                return 'http://127.0.0.1:8000' + self.thumbnail.url #cambiar esta url
            else: 
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
         
        return thumbnail