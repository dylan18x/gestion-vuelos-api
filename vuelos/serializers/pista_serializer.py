from rest_framework import serializers
from vuelos.models.pista import Pista

class PistaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Pista
        fields = '__all__'