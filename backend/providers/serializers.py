from rest_framework import serializers

from providers.models import Product, Provider


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        read_only_fields = ("id", "date_launch")
        fields = "__all__"
