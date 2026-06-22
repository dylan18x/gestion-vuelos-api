# views.py

from rest_framework import viewsets
from ..models import PuertaEmbarque
from ..serializers import PuertaEmbarqueSerializer

class PuertaEmbarqueViewSet(viewsets.ModelViewSet):
    queryset = PuertaEmbarque.objects.all()
    serializer_class = PuertaEmbarqueSerializer