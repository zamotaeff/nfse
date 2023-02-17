import pytest
from django.urls import reverse

from tests.factories import ProductFactory
from providers.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_detail(api_client):
    """
    Test product detail represent
    :param api_client: Rest framework test client
    :return: None
    """
    products = ProductFactory.create_batch(5)

    response = api_client.get(
        path=reverse('product-detail', args=[products[0].id]),
    )

    assert response.status_code == 200
    assert response.data == ProductSerializer(products[0]).data
