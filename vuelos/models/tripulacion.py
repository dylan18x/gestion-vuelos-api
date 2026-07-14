import uuid

from django.db import models
from .empleado import Empleado
from pathlib import Path
from django.db import models

def tripulacion_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'


class Tripulacion(models.Model):
    id_tripulacion = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=50)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to=tripulacion_image_path, blank=True, null=True)

    class Meta:
        db_table = 'tripulacion'