import uuid

from django.db import models
from pathlib import Path
from django.db import models


def incidente_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Incidente(models.Model):
    descripcion = models.TextField()
    fecha       = models.DateField()
    id_vuelo    = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='incidentes',
        db_column='id_vuelo',
    )
    image       = models.ImageField(upload_to=incidente_image_path, blank=True, null=True)

    class Meta:
        verbose_name        = 'Incidente'
        verbose_name_plural = 'Incidentes'
        ordering            = ['-fecha']

    def __str__(self):
        return f'Incidente {self.id} — {self.fecha}'