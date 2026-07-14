import uuid

from django.db import models
from pathlib import Path
from django.db import models


def historial_estado_vuelo_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class HistorialEstadoVuelo(models.Model):
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    observacion  = models.TextField(blank=True, default='')
    id_vuelo     = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='historial_estados',
        db_column='id_vuelo',
    )
    id_estado    = models.ForeignKey(
        'vuelos.EstadoVuelo',
        on_delete=models.PROTECT,
        related_name='historial_estados',
        db_column='id_estado',
    )
    image       = models.ImageField(upload_to=historial_estado_vuelo_image_path, blank=True, null=True)

    class Meta:
        verbose_name        = 'Historial Estado Vuelo'