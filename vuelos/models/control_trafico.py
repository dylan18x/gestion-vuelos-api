import uuid

from django.db import models
from pathlib import Path
from django.db import models


def control_trafico_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class ControlTrafico(models.Model):
    autorizacion = models.CharField(max_length=100)
    hora         = models.DateTimeField()
    image       = models.ImageField(upload_to=control_trafico_image_path, blank=True, null=True)
    id_vuelo     = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='controles_trafico',
        db_column='id_vuelo',
    )

    class Meta:
        verbose_name        = 'Control de Tráfico'
        verbose_name_plural = 'Controles de Tráfico'
        ordering            = ['hora']

    def __str__(self):
        return f'Control {self.id} — Vuelo {self.id_vuelo}'