from rest_framework import serializers
from vuelos.models.asignacion_tripulacion import AsignacionTripulacion

class AsignacionTripulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionTripulacion
        fields = '__all__'