from rest_framework import serializers
from vuelos.models import HistorialEstadoVuelo
from vuelos.serializers.estado_vuelo_serializer import EstadoVueloSerializer


class HistorialEstadoVueloSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        id_estado = EstadoVueloSerializer(read_only=True)
        model  = HistorialEstadoVuelo
        fields = ['id', 'fecha_cambio', 'observacion', 'id_vuelo', 'id_estado']
        read_only_fields = ['id', 'fecha_cambio']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.id_estado:
            representation['id_estado'] = {
                'id': instance.id_estado.id_estado,
                'nombre_estado': instance.id_estado.nombre_estado
            }
        return representation