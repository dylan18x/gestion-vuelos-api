from rest_framework import serializers
from vuelos.models.asignacion_pista import AsignacionPista

class AsignacionPistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionPista
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.id_vuelo:
            representation['id_vuelo'] = {
                'id': instance.id_vuelo.id,
                'codigo_vuelo': instance.id_vuelo.codigo_vuelo,
                'fecha': instance.id_vuelo.fecha,
                'estado': instance.id_vuelo.estado
            }

        if instance.id_pista:
            representation['id_pista'] = {
                'id': instance.id_pista.id_pista,
                'codigo': instance.id_pista.codigo,
                'estado': instance.id_pista.estado
            }

        return representation