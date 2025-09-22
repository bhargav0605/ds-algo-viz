import asyncio
import logging
import json
import websockets
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from typing import Any, Dict

from utils import generate_array
from algorithms.registry import get_by_input

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

async def handler(ws):
    peer = ws.remote_address
    logging.info("Client connected: %s", peer)

    async def send_event(ev):
        try:
            await ws.send(json.dumps(ev))
        except websockets.ConnectionClosed:
            raise

    try:
        async for message in ws:
            logging.info("Received from %s: %r", peer, message)
            data = json.loads(message)
            event_type = data["type"]
            cmd = data["cmd"]
            sorting = data["sorting"]
            minSize = data["minSize"]
            maxSize = data["maxSize"]
            minRange = data["minRange"]
            maxRange = data["maxRange"]

            sorting_normalized = sorting.strip().lower()

            match sorting_normalized:
                case "bs":
                    print("bubble sort")
                    if event_type == "random" and cmd == "generate":
                        genArray = generate_array(minRange, maxRange, minSize, maxSize)
                        try:
                            # Resolve and call registered algorithm (same signature)
                            algo = get_by_input(sorting_normalized)
                            await algo(arr=genArray, send_event=send_event, data=data)
                        except websockets.ConnectionClosed:
                            print("Client disconnected; stopping sorting.")

    except ConnectionClosedOK:
        logging.info("Connection closed normally by client: %s", peer)
    except ConnectionClosedError as e:
        logging.warning("Connection closed with error from %s: %s", peer, e)
    except Exception as e:
        logging.exception("Unexpected error in handler for %s: %s", peer, e)
    finally:
        logging.info("Client disconnected: %s", peer)
