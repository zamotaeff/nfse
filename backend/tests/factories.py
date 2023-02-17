from datetime import datetime

import factory.fuzzy

from providers.models import Product, Provider
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("first_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("safe_email")
    password = factory.Faker("password")

    class Meta:
        model = User


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    model = factory.Faker("first_name")
    date_launch = factory.fuzzy.FuzzyNaiveDateTime(datetime(2023, 1, 1))

    class Meta:
        model = Product


class ProviderFactory(factory.django.DjangoModelFactory):
    type = factory.fuzzy.FuzzyInteger(0, 3)
    title = factory.Faker("name")
    email = factory.Faker("email")
    country = factory.Faker("country")
    city = factory.Faker("city")
    street = factory.Faker("name")
    house_number = factory.fuzzy.FuzzyInteger(0, 30)

    class Meta:
        model = Provider
