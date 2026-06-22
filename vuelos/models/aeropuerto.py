# models.py

from django.db import models

class Aeropuerto(models.Model):
    id_aeropuerto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_iata = models.CharField(max_length=3, unique=True)

    class Meta:
        db_table = 'aeropuerto'

    def __str__(self):
        return self.nombre