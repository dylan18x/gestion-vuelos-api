import uuid

from django.db import models
from .vuelo import Vuelo
from pathlib import Path
from django.db import models

def autorizacion_vuelo_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class AutorizacionVuelo(models.Model):
    id_autorizacion = models.AutoField(primary_key=True)
    tipo_autorizacion = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20)
    id_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to=autorizacion_vuelo_image_path, blank=True, null=True)

    class Meta:
        db_table = 'autorizacion_vuelo'