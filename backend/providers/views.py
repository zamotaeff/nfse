from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response

from providers.models import Product, Provider
from providers.serializers import ProductSerializer, ProviderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProviderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving providers.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'products']
