from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from providers.models import Product, Provider
from providers.serializers import ProductSerializer, ProviderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
