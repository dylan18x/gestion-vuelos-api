from django.db import models
from django.contrib.auth.models import User


class Reserva(models.Model):

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    codigo_reserva = models.CharField(
        max_length=20,
        unique=True
    )

    fecha_reserva = models.DateTimeField(
        auto_now_add=True
    )

    cantidad_pasajeros = models.PositiveIntegerField(
        default=1
    )

    precio_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='confirmada'
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservas'
    )

    vuelo = models.ForeignKey(
        'vuelos.Vuelo',
        on_delete=models.CASCADE,
        related_name='reservas'
    )

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-fecha_reserva']

    def __str__(self):
        return f'{self.codigo_reserva}'