import uuid
from django.db import models
from .vuelo import Vuelo
from .pista import Pista
from pathlib import Path
from django.db import models

def asignacion_pista_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class AsignacionPista(models.Model):
    id_asignacion_pista = models.AutoField(primary_key=True)
    id_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    id_pista = models.ForeignKey(Pista, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to=asignacion_pista_image_path, blank=True, null=True)

    class Meta:
        db_table = 'asignacion_pista'