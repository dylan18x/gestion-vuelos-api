# models.py

import uuid

from django.db import models
from pathlib import Path
from django.db import models


def mantenimiento_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablass/{uuid.uuid4()}{ext}'

class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)

    id_avion = models.ForeignKey(
        'Avion',
        on_delete=models.CASCADE,
        db_column='id_avion',
        related_name='mantenimientos'
    )
    image       = models.ImageField(upload_to=mantenimiento_image_path, blank=True, null=True)

    class Meta:
        db_table = 'mantenimiento'

    def __str__(self):
        return f"Mantenimiento {self.id_mantenimiento} - {self.estado}"