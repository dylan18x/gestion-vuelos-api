from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models           import Ruta
from vuelos.serializers.ruta import RutaSerializer
from vuelos.permissions      import IsStaffOrReadOnly
from vuelos.filters          import RutaFilter
from vuelos.pagination       import StandardPagination


class RutaViewSet(viewsets.ModelViewSet):
    queryset           = Ruta.objects.select_related('origen', 'destino').all()
    serializer_class   = RutaSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_class    = RutaFilter
    ordering_fields    = ['origen', 'destino']
    ordering           = ['origen']