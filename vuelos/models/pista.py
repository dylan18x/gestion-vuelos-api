from django.db import models

class Pista(models.Model):
    id_pista = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'pista'