from typing import List
from fastapi import APIRouter, HTTPException

from order.models.router_model import OrderInput, OrderOutput, Status
from order.repositories.in_memory_repository.in_memory_db import InMemDB
from order.services.order_service import Order


router = APIRouter()
repository = InMemDB()


@router.get('/orders', status_code=200)
async def retrieve_all_orders() -> List[OrderOutput]:
    """
    """
    orders_info = Order(repository).get_all_orders()

    return [
        OrderOutput(
            id=key,
            stoks=val.stoks,
            quantity=val.quantity,
            status=val.status
        )
        for key, val in orders_info.items()
    ]

@router.post('/orders', status_code=201)
def place_a_new_order(order_info: OrderInput) -> OrderOutput:
    """
    """
    new_order_id = Order(repository).post_new_order(order_info.stoks, order_info.quantity)

    return OrderOutput(
        id=new_order_id,
        stoks=order_info.stoks,
        quantity=order_info.quantity,
        status=Status.pending
    )


@router.get('/orders/{order_id}', status_code=200)
def retrieve_a_specific_order(order_id: str) -> OrderOutput:
    """
    """
    if not (order_info := Order(repository).get_specific_order(order_id)):
        raise HTTPException(status_code=404, detail='Order not found!')

    return OrderOutput(
        id=order_id,
        stoks=order_info.stoks,
        quantity=order_info.quantity,
        status=order_info.status
    )


@router.delete('/orders/{order_id}', status_code=204)
def cancel_an_order(order_id: str) -> None:
    """
    """
    Order(repository).delete_existing_order(order_id)


@router.websocket('/ws')
def web_socket_connection_for_real_time_order_information() -> None:
    """
    """
    pass
