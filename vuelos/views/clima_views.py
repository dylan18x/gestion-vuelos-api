# vuelos/views/clima_views.py
from rest_framework import viewsets
from ..models import Clima
from ..serializers import ClimaSerializer
from vuelos.permissions import IsStaffOrReadOnly

class ClimaViewSet(viewsets.ModelViewSet):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer
    permission_classes = [IsStaffOrReadOnly]