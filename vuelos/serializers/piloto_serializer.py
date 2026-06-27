from rest_framework import serializers
from vuelos.models.piloto import Piloto

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'