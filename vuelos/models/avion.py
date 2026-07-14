# models.py

import uuid

from django.db import models
from pathlib import Path
from django.db import models


def avion_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Avion(models.Model):
    id_avion = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    matricula = models.CharField(max_length=20, unique=True)
    image       = models.ImageField(upload_to=avion_image_path, blank=True, null=True)

    id_aerolinea = models.ForeignKey(
        'Aerolinea',
        on_delete=models.CASCADE,
        db_column='id_aerolinea',
        related_name='aviones'
    )


    class Meta:
        db_table = 'avion'

    def __str__(self):
        return f"{self.modelo} - {self.matricula}"