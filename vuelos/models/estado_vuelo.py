# vuelos/models/estado_vuelo.py
from django.db import models

class EstadoVuelo(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50, unique=True) # Para evitar repetidos como (Programado, Retrasado, etc.)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'estado_vuelo' 
        verbose_name = 'Estado de Vuelo'
        verbose_name_plural = 'Estados de Vuelo'

    def __str__(self):
        return self.nombre_estado