# vuelos/views/estado_vuelo_views.py
from rest_framework import viewsets
from ..models import EstadoVuelo
from ..serializers import EstadoVueloSerializer

class EstadoVueloViewSet(viewsets.ModelViewSet):
    queryset = EstadoVuelo.objects.all()
    serializer_class = EstadoVueloSerializer