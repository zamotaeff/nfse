import pytest
from django.urls import reverse

from tests.factories import ProviderFactory


@pytest.mark.django_db
def test_provider_delete(api_client):
    """
    Test provider delete represent
    :param api_client: Rest framework test client
    :return: None
    """
    provider = ProviderFactory.create()

    response = api_client.delete(
        path=reverse('provider-detail', args=[provider.id]),
    )

    assert response.status_code == 204
