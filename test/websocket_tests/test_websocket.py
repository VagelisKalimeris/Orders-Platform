from assertpy import assert_that
from pytest import mark
from websockets import connect

from test.order_tests.test_data.orders.sample_orders import sample_orders


@mark.asyncio
@mark.parametrize('order', sample_orders)
async def test_websocket_connection(orders_test_client, order):

    async with connect('ws://0.0.0.0:80/ws') as websocket:
        # Make api call, verify status
        orders_test_client.post('/orders', order.__dict__)

        # Receive websocket response
        response = await websocket.recv()

        # Verify websocket response
        assert_that(response)
