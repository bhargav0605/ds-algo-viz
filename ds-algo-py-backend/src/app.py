from flask import Flask, request, jsonify
from src.algorithms.bubble_sort import bubble_sort
from src.redis_handler import redis_conn, generate_stream_id_and_key
from typing import List

app = Flask(__name__)

@app.get("/health")
def health(): return {"ok": True}, 200

@app.route('/', methods=["POST"])
def sort_array():
    data = request.get_json()

    sorting = data["sorting"]
    array = data["array"]
    user_id = data["user_id"]
    run_id = data["run_id"]

    stream_key, stream_id = generate_stream_id_and_key(user_id, run_id) 
    match sorting:
        case "bs":
            return bubble_sort(stream_key=stream_key, stream_id=stream_id, array=array)
        case _:
            return "hello"
    