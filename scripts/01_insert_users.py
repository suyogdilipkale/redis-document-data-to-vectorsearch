import redis
import json
import random
from datetime import datetime, timedelta

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Insert dummy data
for i in range(1, 10):
    user_id = f"u{i}"
    portfolio = [
        {"stock": "AAPL", "quantity": random.randint(1, 20), "gainLoss": round(random.uniform(-10, 25), 2)},
        {"stock": "TSLA", "quantity": random.randint(1, 10), "gainLoss": round(random.uniform(-15, 30), 2)},
        {"stock": "HDFC Bank", "quantity": random.randint(1, 20), "gainLoss": round(random.uniform(-10, 25), 2)},
        {"stock": "Axis Bank", "quantity": random.randint(1, 10), "gainLoss": round(random.uniform(-15, 30), 2)},
        {"stock": "Reliance", "quantity": random.randint(1, 20), "gainLoss": round(random.uniform(-10, 25), 2)},
        {"stock": "TATA", "quantity": random.randint(1, 10), "gainLoss": round(random.uniform(-15, 30), 2)}
        
    ]
    transactions = [
        {
            "txnId": f"t{i}_{j}",
            "type": random.choice(["BUY", "SELL"]),
            "amount": random.randint(500, 5000),
            "timestamp": (datetime.now() - timedelta(days=j)).isoformat()
        }
        for j in range(10)
    ]
    doc = {
        "userId": user_id,
        "name": f"User {i}",
        "portfolio": portfolio,
        "transactions": transactions
    }
    r.json().set(f"user:{user_id}", "$", doc)

print("Sample user documents inserted.")
