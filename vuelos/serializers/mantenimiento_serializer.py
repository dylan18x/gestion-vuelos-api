# serializers.py

from rest_framework import serializers
from ..models import Mantenimiento

class MantenimientoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Mantenimiento
        fields = '__all__'