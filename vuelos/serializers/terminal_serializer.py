# serializers.py

from rest_framework import serializers
from ..models import Terminal

class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.id_aeropuerto:
            representation['id_aeropuerto'] = {
                'id': instance.id_aeropuerto.id_aeropuerto,
                'nombre': instance.id_aeropuerto.nombre,
                'ciudad': instance.id_aeropuerto.ciudad,
                'pais': instance.id_aeropuerto.pais,
                'codigo_iata': instance.id_aeropuerto.codigo_iata
            }

        return representation