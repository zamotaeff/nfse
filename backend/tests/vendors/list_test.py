import pytest
from django.urls import reverse

from tests.factories import ProviderFactory


@pytest.mark.django_db
def test_providers_list(api_client):
    """
    Test provider list represent
    :param api_client: Django REST framework test client
    :return: None
    """
    providers = ProviderFactory.create_batch(10)

    response = api_client.get(
        path=reverse('provider-list'),
    )

    assert response.status_code == 200
    assert len(response.data['results']) == 10
