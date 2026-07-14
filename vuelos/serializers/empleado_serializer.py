from rest_framework import serializers
from vuelos.models.empleado import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Empleado
        fields = ['id_empleado', 'nombre', 'cargo']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = representation.pop('id_empleado')
        return representation