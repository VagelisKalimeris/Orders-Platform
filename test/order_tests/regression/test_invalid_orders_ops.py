from pytest import mark, param

from test.order_tests.test_data.orders.sample_orders import invalid_order_id


class TestInvalidOrdersOps:
    def test_retrieve_a_missing_order(self, orders_test_client):
        # Make api call, verify invalid status & message
        orders_test_client.get(f'/orders/{invalid_order_id}', status_code=404, detail='Order not found!')

    def test_cancel_a_missing_order(self, orders_test_client):
        # Make api call, verify invalid status & message
        orders_test_client.delete(f'/orders/{invalid_order_id}', status_code=404, detail='Order not found!')

    @mark.parametrize('invalid_order', [
        # Stoks
        param({'quantity': 33.5}, id='Attribute stoks missing'),
        param({'stoks': None, 'quantity': 33.5}, id='Attribute stoks empty'),
        param({'stiks': 'GBPUSD', 'quantity': 33.5}, id='Attribute stoks invalid name'),
        # Quantity
        param({'stoks': 'GBPUSD'}, id='Attribute quantity missing'),
        param({'stoks': 'GBPUSD', 'quantity': None}, id='Attribute quantity empty'),
        param({'stoks': 'GBPUSD', 'quantiti': 33.5}, id='Attribute quantity invalid name'),
        # Both
        param({}, id='Request body empty')
    ])
    def test_place_an_invalid_order(self, orders_test_client, invalid_order):
        # Make api call, verify invalid status
        orders_test_client.post('/orders', invalid_order, status_code=422)
