from pytest import mark
from assertpy import assert_that

from test.nano_test_framework.response_util import readable_json


@mark.run(order=1)
def test_retrieve_all_orders_with_empty_db(orders_test_client):
    get_resp = orders_test_client.get('/orders')

    assert_that(get_resp, readable_json(get_resp))\
        .is_equal_to([])