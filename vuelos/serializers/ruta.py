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