# vuelos/serializers/clima_serializer.py
from rest_framework import serializers
from ..models import Clima

class ClimaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Clima
        fields = '__all__'