import uuid

from django.db import models
from pathlib import Path
from django.db import models

def vuelo_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'


class Vuelo(models.Model):
    ESTADO_CHOICES = [
        ('programado', 'Programado'),
        ('en_vuelo',   'En Vuelo'),
        ('aterrizado', 'Aterrizado'),
        ('cancelado',  'Cancelado'),
        ('demorado',   'Demorado'),
    ]

    codigo_vuelo = models.CharField(max_length=20, unique=True)
    fecha        = models.DateField()
    estado       = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='programado')
    id_avion     = models.ForeignKey(
        'vuelos.Avion',
        on_delete=models.PROTECT,
        related_name='vuelos',
        db_column='id_avion',
    )
    image       = models.ImageField(upload_to=vuelo_image_path, blank=True, null=True)

    class Meta:
        verbose_name        = 'Vuelo'
        verbose_name_plural = 'Vuelos'
        ordering            = ['fecha', 'codigo_vuelo']

    def __str__(self):
        return f'{self.codigo_vuelo} — {self.fecha}'