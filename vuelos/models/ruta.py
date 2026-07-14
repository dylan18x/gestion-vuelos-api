import uuid

from django.db import models
from pathlib import Path
from django.db import models

def ruta_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Ruta(models.Model):
    origen  = models.ForeignKey(
        'vuelos.Aeropuerto',
        on_delete=models.PROTECT,
        related_name='rutas_origen',
        db_column='origen',
    )
    destino = models.ForeignKey(
        'vuelos.Aeropuerto',
        on_delete=models.PROTECT,
        related_name='rutas_destino',
        db_column='destino',
    )
    image       = models.ImageField(upload_to=ruta_image_path, blank=True, null=True)

    class Meta:
        verbose_name        = 'Ruta'
        verbose_name_plural = 'Rutas'
        ordering            = ['origen', 'destino']
        unique_together     = [['origen', 'destino']]

    def __str__(self):
        return f'{self.origen} → {self.destino}'