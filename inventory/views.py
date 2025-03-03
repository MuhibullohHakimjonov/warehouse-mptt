from rest_framework import viewsets
from .models import Location, Product
from .serializers import LocationSerializer, ProductSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        product_name = self.request.query_params.get("name")
        if product_name is not None:
            queryset = queryset.filter(name=product_name)
        return queryset
