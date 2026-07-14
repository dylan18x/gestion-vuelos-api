from django.db import models
from .vuelo import Vuelo

class AutorizacionVuelo(models.Model):
    id_autorizacion = models.AutoField(primary_key=True)
    tipo_autorizacion = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20)
    id_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'autorizacion_vuelo'