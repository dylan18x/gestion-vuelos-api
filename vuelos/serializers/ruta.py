from rest_framework import serializers
from vuelos.models import Ruta


class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Ruta
        fields = ['id', 'origen', 'destino']
        read_only_fields = ['id']

    def validate(self, data):
        if data.get('origen') == data.get('destino'):
            raise serializers.ValidationError('El origen y destino no pueden ser el mismo aeropuerto.')
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.origen:
            representation['origen'] = {
                'id': instance.origen.id_aeropuerto,
                'nombre': instance.origen.nombre,
                'ciudad': instance.origen.ciudad,
                'codigo_iata': instance.origen.codigo_iata,
            }
            
        if instance.destino:
            representation['destino'] = {
                'id': instance.destino.id_aeropuerto,
                'nombre': instance.destino.nombre,
                'ciudad': instance.destino.ciudad,
                'codigo_iata': instance.destino.codigo_iata,
            }
            
        return representation