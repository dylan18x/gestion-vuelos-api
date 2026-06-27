# models.py

from django.db import models

class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)

    id_avion = models.ForeignKey(
        'Avion',
        on_delete=models.CASCADE,
        db_column='id_avion',
        related_name='mantenimientos'
    )

    class Meta:
        db_table = 'mantenimiento'

    def __str__(self):
        return f"Mantenimiento {self.id_mantenimiento} - {self.estado}"