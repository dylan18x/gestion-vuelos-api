# views.py

from rest_framework import viewsets
from ..models import TipoAvion
from ..serializers import TipoAvionSerializer
from vuelos.permissions import EsTecnico

class TipoAvionViewSet(viewsets.ModelViewSet):
    queryset = TipoAvion.objects.all()
    serializer_class = TipoAvionSerializer
    permission_classes = [EsTecnico]