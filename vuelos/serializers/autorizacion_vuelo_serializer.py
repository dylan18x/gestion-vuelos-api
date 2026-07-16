from rest_framework import serializers
from vuelos.models.autorizacion_vuelo import AutorizacionVuelo

class AutorizacionVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorizacionVuelo
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.id_vuelo:
            representation['id_vuelo'] = {
                'id': instance.id_vuelo.id_vuelo,
                'codigo_vuelo': instance.id_vuelo.codigo_vuelo,
                'fecha': instance.id_vuelo.fecha,
                'estado': instance.id_vuelo.estado
            }

        return representation