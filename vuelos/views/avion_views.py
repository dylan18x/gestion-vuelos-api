# views.py

from rest_framework import viewsets
from ..models import Avion
from ..serializers import AvionSerializer
from vuelos.permissions import EsTecnico  

class AvionViewSet(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = AvionSerializer
    permission_classes = [EsTecnico]