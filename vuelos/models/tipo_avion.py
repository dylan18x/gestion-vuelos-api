# models.py

from django.db import models

class TipoAvion(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    alcance = models.IntegerField()

    class Meta:
        db_table = 'tipo_avion'

    def __str__(self):
        return f"{self.fabricante} {self.modelo}"