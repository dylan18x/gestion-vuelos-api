# vuelos/views/clima_views.py
from rest_framework import viewsets
from ..models import Clima
from ..serializers import ClimaSerializer

class ClimaViewSet(viewsets.ModelViewSet):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer