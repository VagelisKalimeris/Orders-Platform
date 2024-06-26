from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from order.repositories.in_memory_repository.in_memory_db import InMemDB
from order.services.order_service import Order

router = APIRouter()
repository = InMemDB()


@router.websocket('/ws')
async def web_socket_connection_for_real_time_order_information(websocket: WebSocket) -> None:
    """
    Keeps track of connected clients.
    Service implementation sends them with order status updates.
    """
    order_service = Order(repository)

    await websocket.accept()

    await order_service.add_subscribed_websocket_client(websocket)

    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()

    except WebSocketDisconnect:
        await order_service.remove_subscribed_websocket_client(websocket)
