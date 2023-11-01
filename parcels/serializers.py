from rest_framework import serializers
from .models import Letters, Parcels


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = '__all__'


class ParcelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = '__all__'
