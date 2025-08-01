import redis
import numpy as np
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

for i in range(1, 6):
    vector = np.random.rand(8).astype(np.float32).tolist()
    doc = {
        "id": f"v{i}",
        "title": f"Vector Item {i}",
        "embedding": vector
    }
    r.json().set(f"vector:{i}", "$", doc)
print("Inserted dummy vector documents.")