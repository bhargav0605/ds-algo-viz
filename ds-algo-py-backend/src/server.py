import asyncio
import logging
import websockets
import json
import time

from typing import List, Any, Dict 
from helper.constant import SHORT_FORMS, LONG_FORMS 
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

HOST = "localhost"
PORT = 8765

def create_response(type: str, cmd: str, i: int, j: int, array: List[Any]) -> Dict:
    res = {
        "type": type,
        "cmd": cmd,
        "i": i,
        "j": j,
        "array": array
    }
    return res
async def bubblesort(arr: List, send_event):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # Send event when comparing
            res = create_response("define", "compare", j, j+1, arr)
            await send_event(res)
            await asyncio.sleep(3)
            
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Send swapping event
                res = create_response("define", "swap", j, j+1, arr)
                await send_event(res)
                await asyncio.sleep(3.0)
                swapped = True
            # Send no swapp event 
        if (swapped == False):
            break

    # send done event
    res = create_response("define", "done", 0, 0, arr)
    await send_event(res)
    await asyncio.sleep(3.0)
    # return arr

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
            # echo back as text
            data = json.loads(message)
            type = data["type"]
            cmd = data["cmd"]
            array = data["array"]
            sorting = data["sorting"]


            try:
                await bubblesort(array, send_event)
            except websockets.ConnectionClosed:
                print("Client disconnected; stopping sort.")

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
    async with websockets.serve(handler, HOST, PORT):
        logging.info("Server started on ws://%s:%d", HOST, PORT)
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped by user")
