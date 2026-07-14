from rest_framework import serializers
from vuelos.models import ControlTrafico


class ControlTraficoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model  = ControlTrafico
        fields = ['id', 'autorizacion', 'hora', 'id_vuelo']
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.id_vuelo:
            representation['id_vuelo'] = {
                'id': instance.id_vuelo.id,
                'codigo_vuelo': instance.id_vuelo.codigo_vuelo,
                'fecha': instance.id_vuelo.fecha.strftime('%Y-%m-%d') if instance.id_vuelo.fecha else '',
                'estado': instance.id_vuelo.estado,
            }
        return representation