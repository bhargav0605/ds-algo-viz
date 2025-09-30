# src/redis_handler.py
import os
import redis
import time
from dotenv import load_dotenv

# Load environment variables if present
load_dotenv()

redis_conn = redis.Redis(
        host=os.getenv("REDIS_HOST", "127.0.0.1"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        password=os.getenv("REDIS_PASSWORD", None),
        decode_responses=True,
    ) 

def generate_stream_id_and_key(user_id: int, run_id: int):
    millis = int(time.time() * 1000)
    unique_part = f"{user_id}{run_id}"
    stream_id = f"{millis}-{unique_part}"
    stream_key = f"algo:{{{user_id}}}:{run_id}"
    return stream_key, stream_id
