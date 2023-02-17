import pytest
from rest_framework.reverse import reverse

from providers.models import Product


@pytest.mark.django_db
def test_product_create(api_client):
    """
    Test product create
    :param api_client: Django test client
    :return: None
    """

    data = {
        "title": "LCD TV",
        "model": "p1o2i3urrr4"
    }

    response = api_client.post(
        path=reverse('product-list'),
        data=data
    )

    product = Product.objects.last()

    assert response.status_code == 201
    assert response.data['title'] == product.title
