from rest_framework import serializers

from providers.models import Product, Provider


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        read_only_fields = ("id", "date_launch")
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        read_only_fields = ("id", "date_launch", "debts", "type", "date_created")
        fields = "__all__"
