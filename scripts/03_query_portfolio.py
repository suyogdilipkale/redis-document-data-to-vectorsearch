from redis.commands.search.query import Query
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
q = Query('@userId:{u1}').return_fields("$.portfolio").sort_by("gainLoss", asc=False)
res = r.ft("idx:users").search(q)
print(res.docs)