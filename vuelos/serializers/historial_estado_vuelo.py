from rest_framework import serializers
from vuelos.models import HistorialEstadoVuelo


class HistorialEstadoVueloSerializer(serializers.ModelSerializer):
    class Meta:
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