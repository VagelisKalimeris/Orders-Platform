from pytest import mark
from assertpy import assert_that

from test.nano_test_framework.response_util import readable_json
from test.order_tests.test_data.orders.order_test_model import OrderStatus
from test.order_tests.test_data.orders.sample_orders import sample_orders, sample_order_ids, orders_to_delete


class TestOrdersOps:
    def test_retrieve_all_orders_before_insertions(self, orders_test_client):
        # Make api call, verify status
        get_resp = orders_test_client.get('/orders')

        assert_that(get_resp, readable_json(get_resp)) \
            .is_equal_to([])

    @mark.parametrize('order', sample_orders)
    def test_place_a_new_order(self, orders_test_client, order):
        # Make api call, verify status
        post_resp = orders_test_client.post('/orders', order.__dict__)

        new_order_id = assert_that(post_resp, readable_json(post_resp)) \
            .has_stoks(order.stoks) \
            .has_quantity(order.quantity) \
            .has_status(OrderStatus.pending.value) \
            .extract_key('id') \
            .val

        sample_order_ids.append(new_order_id)

    def test_retrieve_all_orders_after_insertions(self, orders_test_client):
        # Make api call, verify status
        get_resp = orders_test_client.get('/orders')

        assert_that(get_resp, readable_json(get_resp)) \
            .extracting('id') \
            .is_equal_to(sample_order_ids)

    @mark.parametrize('order_num', range(len(sample_orders)))
    def test_retrieve_a_specific_order(self, orders_test_client, order_num):
        # Make api call, verify status
        get_resp = orders_test_client.get(f'/orders/{sample_order_ids[order_num]}')

        assert_that(get_resp, readable_json(get_resp)) \
            .has_stoks(sample_orders[order_num].stoks) \
            .has_quantity(sample_orders[order_num].quantity)

    @mark.parametrize('order_num', orders_to_delete)
    # Make api call, verify status
    def test_cancel_an_order(self, orders_test_client, order_num):
        orders_test_client.delete(f'/orders/{sample_order_ids[order_num]}')

    @mark.parametrize('order_num', orders_to_delete)
    def test_canceled_order_status(self, orders_test_client, order_num):
        # Make api call, verify status
        get_resp = orders_test_client.get(f'/orders/{sample_order_ids[order_num]}')

        assert_that(get_resp, readable_json(get_resp)) \
            .has_status(OrderStatus.canceled.value)
