# vuelos/models/estado_vuelo.py
import uuid

from django.db import models
from pathlib import Path
from django.db import models

def estado_vuelo_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class EstadoVuelo(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50, unique=True) # Para evitar repetidos como (Programado, Retrasado, etc.)
    descripcion = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=estado_vuelo_image_path, blank=True, null=True)

    class Meta:
        db_table = 'estado_vuelo' # Nombre limpio para pgAdmin
        verbose_name = 'Estado de Vuelo'
        verbose_name_plural = 'Estados de Vuelo'

    def __str__(self):
        return self.nombre_estado