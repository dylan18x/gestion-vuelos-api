from rest_framework import serializers
from vuelos.models import Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Horario
        fields = ['id', 'salida_programada', 'llegada_programada', 'id_vuelo']
        read_only_fields = ['id']

    def validate(self, data):
        if data.get('llegada_programada') <= data.get('salida_programada'):
            raise serializers.ValidationError('La llegada programada debe ser posterior a la salida.')
        return data