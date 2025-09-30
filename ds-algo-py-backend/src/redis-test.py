import redis
import time

r = redis.Redis(host="localhost", port= 6379, decode_responses=True, password="supersecret")

# print(f"redis: {r}")

# r.set("foo", "bar")
# r.set("foo1", "bar1")
# r.set("foo2", "bar2")
# print("Added")
# time.sleep(3)
ans = r.get("foo2")
# after_trim = r.ltrim()
print(ans)
# print(after_trim)

ans_de = r.xdel("foo2")
print(ans_de)