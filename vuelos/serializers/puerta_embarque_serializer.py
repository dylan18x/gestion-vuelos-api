# serializers.py

from rest_framework import serializers
from ..models import PuertaEmbarque

class PuertaEmbarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuertaEmbarque
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.id_terminal:
            representation['id_terminal'] = {
                'id': instance.id_terminal.id_terminal,
                'numero': instance.id_terminal.numero,
                'aeropuerto': {
                    'id': instance.id_terminal.id_aeropuerto.id_aeropuerto,
                    'nombre': instance.id_terminal.id_aeropuerto.nombre,
                    'ciudad': instance.id_terminal.id_aeropuerto.ciudad,
                    'pais': instance.id_terminal.id_aeropuerto.pais,
                    'codigo_iata': instance.id_terminal.id_aeropuerto.codigo_iata
                }
            }

        return representation