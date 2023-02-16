import factory

from profiles.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")

    class Meta:
        model = User
