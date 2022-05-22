from django.db import models
from PIL import Image as img
from .utils import image_editor
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    
    def save(self, *args, **kwargs):
        x = image_editor(img.open(self.image))
        buffer = BytesIO()
        x.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "myapp_image"