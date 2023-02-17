import pytest
from django.urls import reverse

from tests.factories import ProductFactory


@pytest.mark.django_db
def test_product_delete(api_client):
    """
    Test product delete represent
    :param api_client: Rest framework test client
    :return: None
    """
    products = ProductFactory.create_batch(5)

    response = api_client.delete(
        path=reverse('product-detail', args=[products[0].id]),
    )

    assert response.status_code == 204
