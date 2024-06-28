
from httpx_ws import connect_ws

"""
A main purely for debugging.
"""

if __name__ == '__main__':

    with connect_ws("http://0.0.0.0:80/ws") as ws:
        while True:
            message = ws.receive_text()
            print(message)
