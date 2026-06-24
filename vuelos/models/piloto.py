from django.db import models
from .empleado import Empleado

class Piloto(models.Model):
    id_piloto = models.AutoField(primary_key=True)
    licencia = models.CharField(max_length=50, unique=True)
    id_empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)

    class Meta:
        db_table = 'piloto'