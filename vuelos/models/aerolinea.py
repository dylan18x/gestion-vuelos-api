# models.py
import uuid
from pathlib import Path
from django.db import models

def product_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'products/{uuid.uuid4()}{ext}'

class Aerolinea(models.Model):
    id_aerolinea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    image       = models.ImageField(upload_to=product_image_path, blank=True, null=True)

    class Meta:
        db_table = 'aerolinea'

    def __str__(self):
        return self.nombre