# views.py

from rest_framework import viewsets
from ..models import Terminal
from ..serializers import TerminalSerializer

class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer