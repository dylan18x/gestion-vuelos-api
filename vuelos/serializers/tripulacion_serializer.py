from rest_framework import serializers
from vuelos.models.tripulacion import Tripulacion

class TripulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tripulacion
        fields = ['id_tripulacion', 'cargo', 'id_empleado']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation['id'] = representation.pop('id_tripulacion')
        
        if instance.id_empleado:
            representation['id_empleado'] = {
                'id': instance.id_empleado.id,
                'nombre': instance.id_empleado.nombre,
                'cargo': instance.id_empleado.cargo,
            }
            
        return representation