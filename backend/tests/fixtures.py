import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories import UserFactory


@pytest.fixture
@pytest.mark.django_db
def api_client():
    """
    Create one stated user and set headers for request
    :return: APIClient instance
    """
    user = UserFactory.create(username='john', email='js@js.com', password='js.sj')

    # products = ProductFactory.create_batch(30)
    # providers = ProviderFactory.create_batch(10)

    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client
