# models.py

from django.db import models

class Terminal(models.Model):
    id_terminal = models.AutoField(primary_key=True)
    numero = models.IntegerField()

    id_aeropuerto = models.ForeignKey(
        'Aeropuerto',
        on_delete=models.CASCADE,
        db_column='id_aeropuerto',
        related_name='terminales'
    )

    class Meta:
        db_table = 'terminal'

    def __str__(self):
        return f"Terminal {self.numero}"