from pytest_factoryboy import register

from .factories import UserFactory, TreeFactory, AccountFactory
from .fixtures import create_scenario  # noqa

register(UserFactory)
register(TreeFactory)
register(AccountFactory)
