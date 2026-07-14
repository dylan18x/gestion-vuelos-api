from rest_framework import serializers
from vuelos.models import Horario


class HorarioSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model  = Horario
        fields = ['id', 'salida_programada', 'llegada_programada', 'id_vuelo']
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.id_vuelo:
            representation['id_vuelo'] = {
                'id': instance.id_vuelo.id,
                'codigo_vuelo': instance.id_vuelo.codigo_vuelo,
                'fecha': str(instance.id_vuelo.fecha),
                'estado': instance.id_vuelo.estado,
            }
        return representation

    def validate(self, data):
        if data.get('llegada_programada') <= data.get('salida_programada'):
            raise serializers.ValidationError('La llegada programada debe ser posterior a la salida.')
        return data