from rest_framework import viewsets
from .models import Letters, Parcels
from .serializers import LettersSerializer, ParcelsSerializer


class LettersViewSet(viewsets.ModelViewSet):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer


class ParcelsViewSet(viewsets.ModelViewSet):
    queryset = Parcels.objects.all()
    serializer_class = ParcelsSerializer
