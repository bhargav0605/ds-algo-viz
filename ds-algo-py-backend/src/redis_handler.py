# src/redis_handler.py
import os
import redis
import time
import logging

from dotenv import load_dotenv
from src.logger import logger

try:
    load_dotenv()
except Exception as e:
    print(f"Failed to load .env file: {e}")

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


def delete_all_streams():
    """Delete all Redis streams and their messages."""
    if not redis_conn:
        logger.error("Redis connection not available. Cannot delete streams.")
        return

    try:
        cursor = 0
        total_deleted = 0
        while True:
            cursor, keys = redis_conn.scan(cursor=cursor)
            for key in keys:
                if redis_conn.type(key) == 'stream':
                    redis_conn.delete(key)
                    total_deleted += 1
                    logger.info(f"🧹 Deleted stream: {key}")
            if cursor == 0:
                break

        logger.info(f"✅ Finished deleting all streams. Total deleted: {total_deleted}")

    except Exception as e:
        logger.error(f"❌ Failed to delete streams: {e}")