from rest_framework import viewsets
from rest_framework.response import Response

from providers.models import Product, Provider
from providers.serializers import ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
