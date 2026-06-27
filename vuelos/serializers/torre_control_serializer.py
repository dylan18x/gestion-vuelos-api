from rest_framework import serializers
from vuelos.models.torre_control import TorreControl

class TorreControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TorreControl
        fields = '__all__'