import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

try:
    r.ft("idx:users").create_index([
        redis.commands.search.field.TagField("$.userId", as_name="userId"),
        redis.commands.search.field.TextField("$.portfolio[*].stock", as_name="stock"),
        redis.commands.search.field.NumericField("$.portfolio[*].gainLoss", as_name="gainLoss"),
        redis.commands.search.field.TextField("$.transactions[*].timestamp", as_name="timestamp")
    ], on='JSON', prefix=['user:'])
    print("Index created successfully.")
except Exception as e:
    print("Index might already exist:", e)