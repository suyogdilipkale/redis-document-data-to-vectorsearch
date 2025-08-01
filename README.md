# Redis SQL to RedisJSON, RediSearch & Vector Search

## Contents
- SQL vs NoSQL
- RedisJSON document model
- RediSearch indexing and querying
- Redis Vector search and RedisVL

## Scripts
Run the Python files in `scripts/` or open the notebooks in `notebooks/`.

## Requirements
```
pip install redis numpy redisvl notebook
```

---

## 📘 SQL to RedisJSON and RediSearch

### ✅ Why SQL to RedisJSON?
- Avoid JOIN complexity
- Faster document reads
- Nested structures supported

### 📌 Sample RedisJSON Document
```json
{
  "userId": "u1",
  "portfolio": [{"stock": "AAPL", "quantity": 10, "gainLoss": 5}],
  "transactions": [{"txnId": "t1", "type": "BUY", "amount": 1000, "timestamp": "2025-07-30T12:00:00Z"}]
}
```

---

## 📘 SQL to RedisJSON and RediSearch

```
FT.SEARCH idx:users "@userId:{u1}" RETURN 1 $.portfolio
FT.SEARCH idx:users "@userId:{u1}" SORTBY $.transactions[*].timestamp DESC RETURN 1 $.transactions
```
---

## 🧠 Redis Vector Search
✳️ What is Vector DB?
✳️ High-dimensional vector similarity search
✳️ For semantic, recommendation, document match

---

## 🔁 Redis vs Other Vector DBs
✳️ Redis supports hybrid search (vector + metadata)
✳️ Real-time response via in-memory ops

---

## 🔍 Vector Index
```
VectorField("$.embedding", "FLAT", {
    "TYPE": "FLOAT32",
    "DIM": 8,
    "DISTANCE_METRIC": "COSINE"
}, as_name="embedding")
```
---

## 🛠️ RedisVL Library
✅ Features
Simplified schema + indexing

Add/search vector documents in 2 lines

Plug into OpenAI, HuggingFace, Cohere embeddings

---

## 🔁 Code Example
```
schema = [SchemaField.name("embedding").vector(dims=8)]
index = SearchIndex("idx:demo", prefix="demo:", schema=schema)
index.create(client)
```
---

## ▶️ Demos
### 📓 Run Jupyter Notebooks
* redis_sql_to_redisjson_demo.ipynb
* redis_vector_and_vl_demo.ipynb

---

#### 🔧 Run Python Scripts
```
python scripts/01_insert_users.py
python scripts/02_create_index.py
python scripts/03_query_portfolio.py
python scripts/04_query_transactions.py
```
---

### 🚀 Requirements
* redis >= 7.2
* redis-py with RedisJSON + RediSearch support
* numpy, redisvl, notebook

---

## Install via:
```
pip install redis numpy redisvl notebook

```
