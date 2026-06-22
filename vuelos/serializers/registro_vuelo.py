from rest_framework import serializers
from vuelos.models import RegistroVuelo


class RegistroVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model  = RegistroVuelo
        fields = ['id', 'hora_real_salida', 'hora_real_llegada', 'id_vuelo']
        read_only_fields = ['id']

    def validate(self, data):
        salida  = data.get('hora_real_salida')
        llegada = data.get('hora_real_llegada')
        if salida and llegada and llegada <= salida:
            raise serializers.ValidationError('La hora real de llegada debe ser posterior a la de salida.')
        return data