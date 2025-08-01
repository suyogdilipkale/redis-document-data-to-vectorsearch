import redis
import json
from datetime import datetime, timedelta
import random

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Generate dummy data
for i in range(1, 6):
    user_id = f"u{i}"
    portfolio = [
        {"stock": "AAPL", "quantity": random.randint(1, 20), "gainLoss": round(random.uniform(-10, 25), 2)},
        {"stock": "TSLA", "quantity": random.randint(1, 10), "gainLoss": round(random.uniform(-15, 30), 2)},
        {"stock": "HDFS Bank", "quantity": random.randint(10, 90), "gainLoss": round(random.uniform(-10, 25), 2)},
        {"stock": "MAXIS Bank", "quantity": random.randint(11, 60), "gainLoss": round(random.uniform(-15, 30), 2)}
    ]
    transactions = [
        {
            "txnId": f"t{i}_{j}",
            "type": random.choice(["BUY", "SELL"]),
            "amount": random.randint(500, 5000),
            "timestamp": (datetime.now() - timedelta(days=j)).isoformat()
        }
        for j in range(3)
    ]
    user_doc = {
        "userId": user_id,
        "name": f"User {i}",
        "portfolio": portfolio,
        "transactions": transactions
    }
    r.json().set(f"user:{user_id}", "$", user_doc)
print("Inserted dummy user documents.")
