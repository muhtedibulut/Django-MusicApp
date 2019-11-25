import redis

r = redis.Redis(host="127.0.0.1", port=6379, charset="utf-8", decode_responses=True)


def counter():
    key = "counter"
    r.incr(key)
    return r.get("counter")
