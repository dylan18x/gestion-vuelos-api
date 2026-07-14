# serializers.py

from rest_framework import serializers
from ..models import Avion

class AvionSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Avion
        fields = '__all__'