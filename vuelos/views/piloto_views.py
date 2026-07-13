from rest_framework import viewsets
from vuelos.models.piloto import Piloto
from vuelos.serializers.piloto_serializer import PilotoSerializer

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    permission_classes = [IsStaffOrReadOnly]