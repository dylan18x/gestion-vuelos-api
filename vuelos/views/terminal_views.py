# views.py

from rest_framework import viewsets
from ..models import Terminal
from ..serializers import TerminalSerializer
from vuelos.permissions import IsStaffOrReadOnly

class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer
    permission_classes = [IsStaffOrReadOnly]