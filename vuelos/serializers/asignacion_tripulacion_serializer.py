from rest_framework import serializers
from vuelos.models.asignacion_tripulacion import AsignacionTripulacion

class AsignacionTripulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionTripulacion
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

        if instance.id_empleado:
            representation['id_empleado'] = {
                'id': instance.id_empleado.id_empleado,
                'nombre': instance.id_empleado.nombre,
                'cargo': instance.id_empleado.cargo
            }

        return representation