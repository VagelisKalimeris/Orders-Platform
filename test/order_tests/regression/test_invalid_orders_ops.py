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
        param({'quantity': 33}, id='Attribute "item" missing'),
        param({'item': None, 'quantity': 33}, id='Attribute item empty'),
        param({'itim': 'banana', 'quantity': 33}, id='Attribute item invalid name'),
        # Quantity
        param({'item': 'banana'}, id='Attribute quantity missing'),
        param({'item': 'banana', 'quantity': None}, id='Attribute quantity empty'),
        param({'item': 'banana', 'quantiti': 33}, id='Attribute quantity invalid name'),
        param({'item': 'banana', 'quantity': "fifty"}, id='Attribute quantity invalid type'),
        # Both
        param({}, id='Request body empty')
    ])
    def test_place_an_invalid_order(self, orders_test_client, invalid_order):
        # Make api call, verify invalid status
        orders_test_client.post('/orders', invalid_order, status_code=422)
