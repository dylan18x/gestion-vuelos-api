# views.py

from rest_framework import viewsets
from ..models import Aeropuerto
from ..serializers import AeropuertoSerializer
from vuelos.permissions import IsStaffOrReadOnly

class AeropuertoViewSet(viewsets.ModelViewSet):
    queryset = Aeropuerto.objects.all()
    serializer_class = AeropuertoSerializer
    permission_classes = [IsStaffOrReadOnly]