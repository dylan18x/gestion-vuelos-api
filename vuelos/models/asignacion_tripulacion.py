from django.db import models
# Importa tu modelo Vuelo aquí
from .vuelo import Vuelo 
from .empleado import Empleado

class AsignacionTripulacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    id_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    class Meta:
        db_table = 'asignacion_tripulacion'