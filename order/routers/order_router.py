from typing import List
from fastapi import APIRouter, HTTPException, WebSocket

from order.models.router_model import OrderInput, OrderOutput, Status

router = APIRouter()



order_example = OrderOutput(id='33', stocks='fff', quantity=50, status=Status.pending)


@router.get('/orders', status_code=200)
async def retrieve_all_orders() -> List[OrderOutput]:
    """
    """

    return [order_example]


@router.post('/orders', status_code=201)
async def place_a_new_order(order_info: OrderInput) -> OrderOutput:
    """
    """

    return order_example

@router.get('/orders/{order_id}', status_code=200)
async def retrieve_a_specific_order(order_id: str) -> OrderOutput:
    """
    """

    return order_example


@router.delete('/orders/{order_id}', status_code=204)
async def cancel_an_order(order_id: str) -> None:
    """
    """
    pass


@router.websocket('/ws')
async def web_socket_connection_for_real_time_order_information() -> None:
    """
    """
    pass
