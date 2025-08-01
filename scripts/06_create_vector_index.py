import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

schema = [
    redis.commands.search.field.TextField("$.title", as_name="title"),
    redis.commands.search.field.VectorField("$.embedding", "FLAT", {
        "TYPE": "FLOAT32",
        "DIM": 8,
        "DISTANCE_METRIC": "COSINE",
        "INITIAL_CAP": 100,
    }, as_name="embedding")
]

try:
    r.ft("idx:vectors").create_index(schema, on="JSON", prefix=["vector:"])
    print("Vector index created successfully.")
except Exception as e:
    print("Vector index might already exist:", e)