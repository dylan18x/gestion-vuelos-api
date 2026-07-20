from rest_framework import serializers

from vuelos.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = [
            'id',
            'codigo_reserva',
            'fecha_reserva',
            'cantidad_pasajeros',
            'precio_total',
            'estado',
            'usuario',
            'vuelo',
        ]

        read_only_fields = [
            'id',
            'codigo_reserva',
            'fecha_reserva',
            'usuario',
            'precio_total',
        ]
    def to_representation(self, instance):

        representation = super().to_representation(instance)

        representation['vuelo'] = {
            'id': instance.vuelo.id,
            'codigo_vuelo': instance.vuelo.codigo_vuelo,
            'fecha': instance.vuelo.fecha,
            'estado': instance.vuelo.estado,
            'precio': instance.vuelo.precio,
        }

        return representation