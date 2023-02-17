import pytest
from django.urls import reverse

from providers.serializers import ProviderSerializer
from tests.factories import ProviderFactory


@pytest.mark.django_db
def test_provider_detail(api_client):
    """
    Test vendor detail represent
    :param api_client: Rest framework test client
    :return: None
    """
    provider = ProviderFactory.create()

    response = api_client.get(
        path=reverse('provider-detail', args=[provider.id], ),
    )
    print(response.data)
    print(ProviderSerializer(provider).data)
    assert response.status_code == 200
    assert response.data == ProviderSerializer(provider).data
