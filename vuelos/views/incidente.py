from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models                 import Incidente
from vuelos.serializers.incidente  import IncidenteSerializer
from vuelos.permissions            import IsStaffOrReadOnly
from vuelos.filters                import IncidenteFilter
from vuelos.pagination             import StandardPagination


class IncidenteViewSet(viewsets.ModelViewSet):
    queryset           = Incidente.objects.select_related('id_vuelo').all()
    serializer_class   = IncidenteSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = IncidenteFilter
    search_fields      = ['descripcion']
    ordering_fields    = ['fecha']
    ordering           = ['-fecha']