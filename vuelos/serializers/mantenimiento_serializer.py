# serializers.py

from rest_framework import serializers
from ..models import Mantenimiento

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.id_avion:
            representation['id_avion'] = {
                'id': instance.id_avion.id_avion,
                'modelo': instance.id_avion.modelo,
                'capacidad': instance.id_avion.capacidad,
                'matricula': instance.id_avion.matricula,
                'aerolinea': {
                    'id': instance.id_avion.id_aerolinea.id_aerolinea,
                    'nombre': instance.id_avion.id_aerolinea.nombre,
                    'pais': instance.id_avion.id_aerolinea.pais
                }
            }

        return representation