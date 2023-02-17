import factory
import pytest
from django.urls import reverse

from tests.factories import UserFactory
from users.serializers import UserCurrentSerializer


@pytest.mark.django_db
def test_users_list(api_client):
    """
    Test user profile
    :param client: Django test client
    :return: None
    """

    response = api_client.get(
        path=reverse('user-list'),
    )

    assert response.status_code == 200
    assert len(response.data['results']) == 1
