import redis
import numpy as np
from redis.commands.search.query import Query

r = redis.Redis(host='localhost', port=6379, decode_responses=False)

query_vector = np.random.rand(8).astype(np.float32).tobytes()
q = Query("*=>[KNN 2 @embedding $vec AS score]").sort_by("score").return_fields("title", "score").dialect(2)
params = {"vec": query_vector}
res = r.ft("idx:vectors").search(q, query_params=params)

for doc in res.docs:
    print(doc.title, doc.score)