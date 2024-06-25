from fastapi import APIRouter, WebSocket

from order.repositories.in_memory_repository.in_memory_db import InMemDB
from order.services.order_service import Order

router = APIRouter()
repository = InMemDB()


@router.websocket('/ws')
async def web_socket_connection_for_real_time_order_information(websocket: WebSocket) -> None:
    """
    Working experiment.
    """
    await websocket.accept()
    while True:
        order_id = await websocket.receive_text()
        if order := await Order(repository).get_specific_order(order_id):
            await websocket.send_text(order.status.value)
        else:
            await websocket.send_text('Invalid order id!')
