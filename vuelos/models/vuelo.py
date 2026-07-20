from django.db import models


class Vuelo(models.Model):
    ESTADO_CHOICES = [
        ('programado', 'Programado'),
        ('en_vuelo', 'En Vuelo'),
        ('aterrizado', 'Aterrizado'),
        ('cancelado', 'Cancelado'),
        ('demorado', 'Demorado'),
    ]

    codigo_vuelo = models.CharField(max_length=20, unique=True)

    fecha = models.DateField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='programado'
    )

    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    asientos_disponibles = models.PositiveIntegerField(
        default=0
    )

    id_avion = models.ForeignKey(
        'vuelos.Avion',
        on_delete=models.PROTECT,
        related_name='vuelos',
        db_column='id_avion'
    )

    class Meta:
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'
        ordering = ['fecha', 'codigo_vuelo']

    def __str__(self):
        return f'{self.codigo_vuelo} — {self.fecha}'