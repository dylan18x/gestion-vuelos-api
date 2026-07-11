from rest_framework import serializers
from vuelos.models.piloto import Piloto

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = ['id_piloto', 'licencia', 'id_empleado']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation['id'] = representation.pop('id_piloto')
        
        if instance.id_empleado:
            representation['id_empleado'] = {
                'id': instance.id_empleado.id_empleado,
                'nombre': instance.id_empleado.nombre,
                'cargo': instance.id_empleado.cargo,
            }
            
        return representation