import uuid

from django.db import models
from pathlib import Path
from django.db import models


def empleado_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    image       = models.ImageField(upload_to=empleado_image_path, blank=True, null=True)

    class Meta:
        db_table = 'empleado'

    def __str__(self):
        return self.nombre