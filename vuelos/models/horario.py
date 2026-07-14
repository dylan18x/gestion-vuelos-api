from django.db import models


class Horario(models.Model):
    salida_programada  = models.DateTimeField()
    llegada_programada = models.DateTimeField()
    id_vuelo           = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='horarios',
        db_column='id_vuelo',
    )

    class Meta:
        verbose_name        = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering            = ['salida_programada']

    def __str__(self):
        return f'Horario {self.id} — Vuelo {self.id_vuelo}'