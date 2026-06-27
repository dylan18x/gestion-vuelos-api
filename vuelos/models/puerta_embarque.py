# models.py

from django.db import models

class PuertaEmbarque(models.Model):
    id_puerta = models.AutoField(primary_key=True)
    numero = models.IntegerField()

    id_terminal = models.ForeignKey(
        'Terminal', 
        on_delete=models.CASCADE,
        db_column='id_terminal',
        related_name='puertas_embarque'
    )

    class Meta:
        db_table = 'puerta_embarque'

    def __str__(self):
        return f"Puerta {self.numero}"