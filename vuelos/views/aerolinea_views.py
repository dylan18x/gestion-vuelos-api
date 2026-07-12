# views.py

from rest_framework import viewsets
from ..models import Aerolinea
from ..serializers import AerolineaSerializer

class AerolineaViewSet(viewsets.ModelViewSet):
    queryset = Aerolinea.objects.all()
    serializer_class = AerolineaSerializer