# vuelos/models/clima.py
from django.db import models
from .aeropuerto import Aeropuerto  # Importamos el modelo con el que se relaciona

class Clima(models.Model):
    id_clima = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()  # Registra el día y la hora del reporte climático
    temperatura = models.DecimalField(max_length=5, max_digits=5, decimal_places=2) # Ej: 25.50 o -5.20
    condicion = models.CharField(max_length=100)  # Ej: Soleado, Tormenta, Niebla
    velocidad_viento = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 15.40 km/h
    
    # Relación: Un aeropuerto puede tener muchos registros de clima a lo largo del tiempo
    id_aeropuerto = models.ForeignKey(
        Aeropuerto, 
        on_delete=models.CASCADE, 
        related_name='climas'
    )

    class Meta:
        db_table = 'clima'  # Nombre limpio para tu pgAdmin
        verbose_name = 'Clima'
        verbose_name_plural = 'Climas'

    def __str__(self):
        return f"{self.condicion} - {self.id_aeropuerto.nombre} ({self.fecha})"