from pytest import fixture

from test.nano_test_framework.http_client import OrdersTestClient


pytest_plugins = ['test.nano_test_framework.assertpy_extensions']


@fixture(scope='session')
def orders_test_client():
    """
    Provides test client instance to all module tests.
    """

    yield OrdersTestClient()
