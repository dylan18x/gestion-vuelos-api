import uuid

from django.db import models
from .empleado import Empleado
from pathlib import Path
from django.db import models

def piloto_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Piloto(models.Model):
    id_piloto = models.AutoField(primary_key=True)
    licencia = models.CharField(max_length=50, unique=True)
    id_empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to=piloto_image_path, blank=True, null=True)

    class Meta:
        db_table = 'piloto'