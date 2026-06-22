from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models                      import ControlTrafico
from vuelos.serializers.control_trafico import ControlTraficoSerializer
from vuelos.permissions                 import IsStaffOrReadOnly
from vuelos.filters                     import ControlTraficoFilter
from vuelos.pagination                  import StandardPagination


class ControlTraficoViewSet(viewsets.ModelViewSet):
    queryset           = ControlTrafico.objects.select_related('id_vuelo').all()
    serializer_class   = ControlTraficoSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = ControlTraficoFilter
    search_fields      = ['autorizacion']
    ordering_fields    = ['hora']
    ordering           = ['hora']