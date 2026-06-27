from django.db import models
from .empleado import Empleado

class Tripulacion(models.Model):
    id_tripulacion = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=50)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tripulacion'