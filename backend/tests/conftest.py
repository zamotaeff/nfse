from pytest_factoryboy import register

import tests.factories

register(tests.factories.UserFactory)
register(tests.factories.ProductFactory)
register(tests.factories.ProviderFactory)

pytest_plugins = 'tests.fixtures'
