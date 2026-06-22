from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models              import Horario
from vuelos.serializers.horario import HorarioSerializer
from vuelos.permissions         import IsStaffOrReadOnly
from vuelos.filters             import HorarioFilter
from vuelos.pagination          import StandardPagination


class HorarioViewSet(viewsets.ModelViewSet):
    queryset           = Horario.objects.select_related('id_vuelo').all()
    serializer_class   = HorarioSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_class    = HorarioFilter
    ordering_fields    = ['salida_programada', 'llegada_programada']
    ordering           = ['salida_programada']