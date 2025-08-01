from redisvl.index import SearchIndex
from redisvl.schema import IndexSchema, VectorField, TextField
from redisvl.client import Client
import numpy as np

client = Client()
schema = IndexSchema([
    TextField(name="title"),
    VectorField(name="embedding", dims=8, algorithm="flat", distance_metric="cosine")
])
index = SearchIndex(index_name="vl:idx:vectors", prefix="vl:vector:", schema=schema)
index.create(client)

# Insert a vector
doc = {
    "id": "vl:vector:1",
    "title": "RedisVL Item 1",
    "embedding": np.random.rand(8).astype(np.float32).tolist()
}
client.hset(document=doc)

# Query using KNN
results = index.query().knn("embedding", np.random.rand(8), k=2).return_fields("title").execute(client)
for r in results:
    print(r)