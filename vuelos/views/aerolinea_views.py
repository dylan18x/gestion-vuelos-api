# views.py

from rest_framework import viewsets
from ..models import Aerolinea
from ..serializers import AerolineaSerializer
from vuelos.permissions import EsOperadorVuelo

class AerolineaViewSet(viewsets.ModelViewSet):
    queryset = Aerolinea.objects.all()
    serializer_class = AerolineaSerializer
    permission_classes = [EsOperadorVuelo]