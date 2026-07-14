from rest_framework import serializers
from vuelos.models.asignacion_pista import AsignacionPista

class AsignacionPistaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = AsignacionPista
        fields = '__all__'