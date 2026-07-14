# models.py
import uuid
from pathlib import Path
from django.db import models

def aeropuerto_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'


class Aeropuerto(models.Model):
    id_aeropuerto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_iata = models.CharField(max_length=3, unique=True)
    image       = models.ImageField(upload_to=aeropuerto_image_path, blank=True, null=True)

    class Meta:
        db_table = 'aeropuerto'

    def __str__(self):
        return self.nombre