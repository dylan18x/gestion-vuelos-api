from django.db import models
from .aeropuerto import Aeropuerto

class TorreControl(models.Model):
    id_torre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=20)
    id_aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)

    class Meta:
        db_table = 'torre_control'