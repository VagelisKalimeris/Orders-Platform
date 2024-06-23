from pytest import mark
from assertpy import assert_that

from test.nano_test_framework.response_util import readable_json
from test.order_tests.test_data.orders.sample_orders import sample_orders, sample_order_ids


@mark.run(order=2)
class TestOrdersOps:
    @mark.parametrize('order', sample_orders)
    def test_new_order_placement(self, orders_test_client, order):
        get_resp = orders_test_client.post('/orders', order.__dict__)

        new_order_id = assert_that(get_resp, readable_json(get_resp))\
            .has_stoks(order.stoks)\
            .has_quantity(order.quantity)\
            .extract_key('id')\
            .val

        sample_order_ids.append(new_order_id)