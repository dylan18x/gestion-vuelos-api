import uuid

from django.db import models
from pathlib import Path
from django.db import models


def horario_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Horario(models.Model):
    salida_programada  = models.DateTimeField()
    llegada_programada = models.DateTimeField()
    id_vuelo           = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='horarios',
        db_column='id_vuelo',
    )
    image       = models.ImageField(upload_to=horario_image_path, blank=True, null=True)

    class Meta:
        verbose_name        = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering            = ['salida_programada']

    def __str__(self):
        return f'Horario {self.id} — Vuelo {self.id_vuelo}'