from rest_framework import serializers
from vuelos.models import HistorialEstadoVuelo


class HistorialEstadoVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HistorialEstadoVuelo
        fields = ['id', 'fecha_cambio', 'observacion', 'id_vuelo', 'id_estado']
        read_only_fields = ['id', 'fecha_cambio']