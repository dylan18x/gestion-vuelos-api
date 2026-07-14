import uuid

from django.db import models
# Importa tu modelo Vuelo aquí
from .vuelo import Vuelo 
from .empleado import Empleado
from pathlib import Path
from django.db import models

def asignacion_tripulacion_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'taablas/{uuid.uuid4()}{ext}'

class AsignacionTripulacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    id_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to=asignacion_tripulacion_image_path, blank=True, null=True)

    class Meta:
        db_table = 'asignacion_tripulacion'