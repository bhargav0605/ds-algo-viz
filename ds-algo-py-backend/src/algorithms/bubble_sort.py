from typing import List
from src.redis_handler import redis_conn
from src.event import write_event

import json

def bubble_sort(stream_key: str, stream_id: str, array: List[int]) -> str:
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # Compare Event
            eve = write_event(stream_id=stream_id, stream_key=stream_key,cmd="compare", sorting="bs", array=array, i=j, j=j+1)
            redis_conn.xadd(stream_key, {"event": json.dumps(eve)})
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]

                # Swap Event
                eve = write_event(stream_id=stream_id, stream_key=stream_key, cmd="swap", sorting="bs", array=array, i=j, j=j+1)
                redis_conn.xadd(stream_key, {"event": json.dumps(eve)})

                swapped=True
        if swapped == False:
            break
    
    # Done Event
    eve = write_event(stream_id=stream_id, stream_key=stream_key, cmd="done", sorting="bs", array=array, i=j, j=j+1)
    redis_conn.xadd(stream_key, {"event": json.dumps(eve)})
    return { "status": "started" }