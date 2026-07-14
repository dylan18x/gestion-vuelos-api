import uuid

from django.db import models
from pathlib import Path
from django.db import models


def escala_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Escala(models.Model):
    id_vuelo          = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='escalas',
        db_column='id_vuelo',
    )
    aeropuerto_escala = models.ForeignKey(
        'vuelos.Aeropuerto',
        on_delete=models.PROTECT,
        related_name='escalas',
        db_column='aeropuerto_escala',
    )

    image       = models.ImageField(upload_to=escala_image_path, blank=True, null=True)

    class Meta:
        verbose_name        = 'Escala'
        verbose_name_plural = 'Escalas'
        ordering            = ['id_vuelo']
        unique_together     = [['id_vuelo', 'aeropuerto_escala']]

    def __str__(self):
        return f'Escala {self.aeropuerto_escala} — Vuelo {self.id_vuelo}'