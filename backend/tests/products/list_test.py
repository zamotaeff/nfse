import pytest
from django.urls import reverse

from tests.factories import ProductFactory


@pytest.mark.django_db
def test_products_list(api_client):
    """
    Test products list represent
    :param api_client: Django REST framework test client
    :return: None
    """
    products = ProductFactory.create_batch(10)

    response = api_client.get(
        path=reverse('product-list'),
    )

    assert response.status_code == 200
    assert len(response.data['results']) == 10
