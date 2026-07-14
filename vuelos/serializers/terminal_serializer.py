# serializers.py

from rest_framework import serializers
from ..models import Terminal

class TerminalSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Terminal
        fields = '__all__'