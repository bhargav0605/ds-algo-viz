from typing import List, Dict

def write_event(
        stream_id: str,
        stream_key: str,
        cmd: str, 
        sorting: str, 
        array: List[int], 
        i: int, 
        j: int) -> Dict:
    return {
        "stream_id": stream_id,
        "stream_key": stream_key,
        "cmd": cmd,
        "sorting": sorting,
        "array": array,
        "i": i,
        "j": j
    }