# models.py

import uuid

from django.db import models
from pathlib import Path
from django.db import models

def tipo_avion_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'


class TipoAvion(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    alcance = models.IntegerField()
    image       = models.ImageField(upload_to=tipo_avion_image_path, blank=True, null=True)

    class Meta:
        db_table = 'tipo_avion'

    def __str__(self):
        return f"{self.fabricante} {self.modelo}"