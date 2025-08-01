import redis, json, random
from datetime import datetime, timedelta

r = redis.Redis(decode_responses=True)
for i in range(3):
    r.json().set(f"user:u{i}", "$", {
        "userId": f"u{i}",
        "name": f"User {i}",
        "portfolio": [{"stock": "AAPL", "quantity": 10, "gainLoss": 5}],
        "transactions": [{"txnId": f"t{i}", "type": "BUY", "amount": 1000, "timestamp": datetime.utcnow().isoformat()}]
    })
print("Inserted users.")
