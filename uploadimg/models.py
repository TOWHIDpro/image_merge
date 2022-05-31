from django.db import models
from .utils import image_editor
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

class ImageModel(models.Model):
    img_front = models.ImageField(upload_to='images', blank=True)
    img_back = models.ImageField(upload_to='images', blank=True)
    
    # We Will use this later if we want databas interaction------------------------------------------
    def save(self, image_front, image_back, color, position, *args, **kwargs):
        img_f, img_b = image_editor(image_front, image_back, color, position)

        if img_f:
            buffer_f = BytesIO()
            img_f.save(buffer_f, format='png')
            image_png_f = buffer_f.getvalue()
            self.img_front.save(str(self.img_front), ContentFile(image_png_f), save=False)

        if img_b:
            buffer_b = BytesIO()
            img_b.save(buffer_b, format='png')
            image_png_b = buffer_b.getvalue()
            self.img_back.save(str(self.img_back), ContentFile(image_png_b), save=False)

        super().save(*args, **kwargs)

    class Meta:
        db_table = "myapp_image"