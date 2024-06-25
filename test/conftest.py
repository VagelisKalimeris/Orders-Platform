from pytest import fixture

from test.nano_test_framework.http_client import OrdersTestClient
from test.nano_test_framework.load_test_client import LoadTestClient

pytest_plugins = ['test.nano_test_framework.assertpy_extensions']


@fixture(scope='session')
def orders_test_client():
    """
    Provides test client instance to all module tests.
    """

    yield OrdersTestClient()


@fixture(scope='session')
def load_test_client():
    """
    Provides load test client instance to all module tests.
    """

    yield LoadTestClient()