from django.db import models


class RegistroVuelo(models.Model):
    hora_real_salida  = models.DateTimeField(null=True, blank=True)
    hora_real_llegada = models.DateTimeField(null=True, blank=True)
    id_vuelo          = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='registros',
        db_column='id_vuelo',
    )

    class Meta:
        verbose_name        = 'Registro de Vuelo'
        verbose_name_plural = 'Registros de Vuelo'
        ordering            = ['id_vuelo']

    def __str__(self):
        return f'Registro {self.id} — Vuelo {self.id_vuelo}'