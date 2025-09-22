import random
import asyncio
import logging
import websockets
import json
import time
import numpy

from typing import List, Any, Dict, Optional
from helper.constant import SHORT_FORMS, LONG_FORMS 
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

HOST = "localhost"
PORT = 8765

def create_response(
        event_type: str, 
        cmd: str,
        sorting: str, 
        array: Optional[List[Any]]=None,
        minSize: int = 0,
        maxSize: int = 0,
        minRange: int = 0,
        maxRange: int = 0,
        i: int = 0, 
        j: int=0) -> Dict:
    return {
        "type": event_type,
        "cmd": cmd,
        "array": array,
        "sorting": sorting,
        "minSize": minSize,
        "maxSize": maxSize,
        "minRange": minRange,
        "maxRange": maxRange,
        "i": i,
        "j": j,
    }
async def bubblesort(arr: List, send_event, data: Dict[str, Any]):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # Send event when comparing
            res = create_response(event_type=data["type"], cmd="compare", i=j, j=j+1, array=arr, sorting=data["sorting"])
            await send_event(res)
            await asyncio.sleep(3)
            
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Send swapping event
                res = create_response(event_type=data["type"], cmd="swap", i=j, j=j+1, array=arr, sorting=data["sorting"])
                print(f"Response: {res}")
                await send_event(res)
                await asyncio.sleep(3.0)
                swapped = True
            # Send no swapp event 
        if (swapped == False):
            break

    # send done event
    res = create_response(event_type=data["type"], cmd="done", array=arr, sorting=data["sorting"])
    await send_event(res)
    await asyncio.sleep(3.0)
    # return arr

# Generating an array here
def generate_array(minRange: int, maxRange: int, minSize: int, maxSize: int):
    print("Generating number")
    size_array = random.randint(minSize, maxSize)
    print(f"Size of an array is {size_array}")

    random_integers_1D = numpy.random.randint(minRange, maxRange, size=size_array)
    return random_integers_1D.tolist()



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
                            await bubblesort(arr=genArray, send_event=send_event, data=data)
                        except websockets.ConnectionClosed:
                            print("Client disconnected; stopping sorting.")

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
