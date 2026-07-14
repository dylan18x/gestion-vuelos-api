from django.db import models


class ControlTrafico(models.Model):
    autorizacion = models.CharField(max_length=100)
    hora         = models.DateTimeField()
    id_vuelo     = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='controles_trafico',
        db_column='id_vuelo',
    )

    class Meta:
        verbose_name        = 'Control de Tráfico'
        verbose_name_plural = 'Controles de Tráfico'
        ordering            = ['hora']

    def __str__(self):
        return f'Control {self.id} — Vuelo {self.id_vuelo}'