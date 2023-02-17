from rest_framework import serializers

from providers.models import Product, Provider


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    def validate(self, data):
        instance = self.instance
        if instance:
            original_debts = instance.debts
            new_debts = data.get('debts')
            # Если кто нибудь посмеет изменить задолженность через API
            # мы окажемся на шаг впереди и просто
            # изменим входящие данные на оригинал
            if new_debts and (new_debts != original_debts):
                data.update({'debt': original_debts})
        return data

    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Provider
        fields = '__all__'
