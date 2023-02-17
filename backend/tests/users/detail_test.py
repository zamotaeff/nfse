import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_user_profile(api_client):
    """
    Test user profile
    :param api_client: Rest framework test client
    :return: None
    """

    user = User.objects.last()

    response = api_client.get(
        path=reverse('user-detail', args=[user.id, ]),
    )

    assert response.status_code == 200
    assert response.data['email'] == user.email
