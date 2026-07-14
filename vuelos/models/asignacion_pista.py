from django.db import models
from .vuelo import Vuelo
from .pista import Pista

class AsignacionPista(models.Model):
    id_asignacion_pista = models.AutoField(primary_key=True)
    id_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    id_pista = models.ForeignKey(Pista, on_delete=models.CASCADE)

    class Meta:
        db_table = 'asignacion_pista'