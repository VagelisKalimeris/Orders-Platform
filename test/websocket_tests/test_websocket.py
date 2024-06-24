from httpx import AsyncClient


"""
A main purely for debugging.
"""
if __name__ == '__main__':
    client = AsyncClient()
    ws = client.websocket('0.0.0.0:80/ws')
    ws.send_text('put uuid here')
    received_status = ws.receive_text()
    print(f'Status: {received_status}')
