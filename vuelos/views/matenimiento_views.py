# views.py

from rest_framework import viewsets
from ..models import Mantenimiento
from ..serializers import MantenimientoSerializer
from vuelos.permissions import EsTecnico 

class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [EsTecnico]