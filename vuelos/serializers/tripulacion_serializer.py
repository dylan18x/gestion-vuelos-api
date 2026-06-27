from rest_framework import serializers
from vuelos.models.tripulacion import Tripulacion

class TripulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tripulacion
        fields = '__all__'