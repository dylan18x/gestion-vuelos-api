from django.db import models


class Incidente(models.Model):
    descripcion = models.TextField()
    fecha       = models.DateField()
    id_vuelo    = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='incidentes',
        db_column='id_vuelo',
    )

    class Meta:
        verbose_name        = 'Incidente'
        verbose_name_plural = 'Incidentes'
        ordering            = ['-fecha']

    def __str__(self):
        return f'Incidente {self.id} — {self.fecha}'