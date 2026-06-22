from django.db import models


class Ruta(models.Model):
    origen  = models.ForeignKey(
        'store.Aeropuerto',
        on_delete=models.PROTECT,
        related_name='rutas_origen',
        db_column='origen',
    )
    destino = models.ForeignKey(
        'store.Aeropuerto',
        on_delete=models.PROTECT,
        related_name='rutas_destino',
        db_column='destino',
    )

    class Meta:
        verbose_name        = 'Ruta'
        verbose_name_plural = 'Rutas'
        ordering            = ['origen', 'destino']
        unique_together     = [['origen', 'destino']]

    def __str__(self):
        return f'{self.origen} → {self.destino}'