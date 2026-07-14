import uuid

from django.db import models
from .aeropuerto import Aeropuerto
from pathlib import Path
from django.db import models

def torre_control_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'


class TorreControl(models.Model):
    id_torre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=20)
    id_aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to=torre_control_image_path, blank=True, null=True)

    class Meta:
        db_table = 'torre_control'