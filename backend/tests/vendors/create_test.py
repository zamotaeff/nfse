import pytest
from rest_framework.reverse import reverse

from providers.models import Provider


@pytest.mark.django_db
def test_provider_create(api_client):
    """
    Test provider create
    :param api_client: Django test client
    :return: None
    """

    data = {
        "title": "UralMash",
        "type": 0,
        "email": "test_email@mail.ru",
        "country": "Russia",
        "city": "Moscow",
        "street": "Gukovskay",
        "house_number": "1"
    }

    response = api_client.post(
        path=reverse('provider-list'),
        data=data
    )

    vendor = Provider.objects.last()

    assert response.status_code == 201
    assert response.data['title'] == vendor.title
