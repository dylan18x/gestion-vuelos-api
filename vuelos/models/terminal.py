# models.py

import uuid

from django.db import models
from pathlib import Path
from django.db import models

def terminal_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'


class Terminal(models.Model):
    id_terminal = models.AutoField(primary_key=True)
    numero = models.IntegerField()

    id_aeropuerto = models.ForeignKey(
        'Aeropuerto',
        on_delete=models.CASCADE,
        db_column='id_aeropuerto',
        related_name='terminales'
    )
    image       = models.ImageField(upload_to=terminal_image_path, blank=True, null=True)

    class Meta:
        db_table = 'terminal'

    def __str__(self):
        return f"Terminal {self.numero}"