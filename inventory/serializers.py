from rest_framework import serializers
from .models import Location, Product

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'parent']

class ProductSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'type', 'location']