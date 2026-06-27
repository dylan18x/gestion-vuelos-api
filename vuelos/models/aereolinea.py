# models.py

from django.db import models

class Aerolinea(models.Model):
    id_aerolinea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    class Meta:
        db_table = 'aerolinea'

    def __str__(self):
        return self.nombre