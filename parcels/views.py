from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Letters, Parcels
from .serializers import LettersSerializer, ParcelsSerializer


class LettersViewSet(viewsets.ModelViewSet):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer


class ParcelsViewSet(viewsets.ModelViewSet):
    queryset = Parcels.objects.all()
    serializer_class = ParcelsSerializer

# class LetterAPIView(APIView):
#     def get(self, request):
#         return Response({'tittle': 'Custom_letter'})


# class LetterAPIView(generics.ListAPIView):
#     queryset = Letters.objects.all()
#     serializer_class = LettersSerializer
#
#
# class ParcelAPIView(generics.ListAPIView):
#     queryset = Parcels.objects.all()
#     serializer_class = ParcelsSerializer
