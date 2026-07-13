from rest_framework import viewsets
from vuelos.models.torre_control import TorreControl
from vuelos.serializers.torre_control_serializer import TorreControlSerializer
from vuelos.permissions import IsStaffOrReadOnly

class TorreControlViewSet(viewsets.ModelViewSet):
    queryset = TorreControl.objects.all()
    serializer_class = TorreControlSerializer
    permission_classes = [IsStaffOrReadOnly]