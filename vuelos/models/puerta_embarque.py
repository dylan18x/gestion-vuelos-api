# models.p
import uuid

from django.db import models
from pathlib import Path
from django.db import models

def puerta_embarque_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class PuertaEmbarque(models.Model):
    id_puerta = models.AutoField(primary_key=True)
    numero = models.IntegerField()

    id_terminal = models.ForeignKey(
        'Terminal', 
        on_delete=models.CASCADE,
        db_column='id_terminal',
        related_name='puertas_embarque'
    )
    image       = models.ImageField(upload_to=puerta_embarque_image_path, blank=True, null=True)

    class Meta:
        db_table = 'puerta_embarque'

    def __str__(self):
        return f"Puerta {self.numero}"