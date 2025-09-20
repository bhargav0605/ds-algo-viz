# server.py
import asyncio
import logging
import websockets
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

HOST = "localhost"
PORT = 8765

async def echo(ws):
    peer = ws.remote_address
    logging.info("Client connected: %s", peer)
    try:
        async for message in ws:
            # message can be str or bytes
            logging.info("Received from %s: %r", peer, message)
            # echo back as text
            await ws.send(f"Echo: {message}")
    except ConnectionClosedOK:
        logging.info("Connection closed normally by client: %s", peer)
    except ConnectionClosedError as e:
        logging.warning("Connection closed with error from %s: %s", peer, e)
    except Exception as e:
        # This will print the actual exception you were missing before
        logging.exception("Unexpected error in handler for %s: %s", peer, e)
    finally:
        logging.info("Client disconnected: %s", peer)

async def main():
    async with websockets.serve(echo, HOST, PORT):
        logging.info("Server started on ws://%s:%d", HOST, PORT)
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped by user")
