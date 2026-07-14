from django.db import models


class HistorialEstadoVuelo(models.Model):
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    observacion  = models.TextField(blank=True, default='')
    id_vuelo     = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='historial_estados',
        db_column='id_vuelo',
    )
    id_estado    = models.ForeignKey(
        'vuelos.EstadoVuelo',
        on_delete=models.PROTECT,
        related_name='historial_estados',
        db_column='id_estado',
    )

    class Meta:
        verbose_name        = 'Historial Estado Vuelo'