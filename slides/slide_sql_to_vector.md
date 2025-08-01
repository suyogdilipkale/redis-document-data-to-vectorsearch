# Slide 1: Why You Need SQL to RedisJSON and RediSearch

- Traditional RDBMS struggles with performance at scale.
- JSON document modeling matches modern app needs.
- RedisJSON stores rich objects; RediSearch provides fast querying.
- Enables schema-less, nested object storage with full-text search and filtering.

---

# Slide 2: SQL vs NoSQL Comparison

| Feature              | SQL (RDBMS)     | NoSQL (RedisJSON + RediSearch) |
|----------------------|----------------|-------------------------------|
| Schema               | Fixed          | Dynamic                       |
| Performance at scale | Limited        | High                          |
| Nested data          | Complex joins  | Native in JSON                |
| Search               | Indexes only   | Full-text, range, tag, geo    |

---

# Slide 3: What is RedisJSON and RediSearch?

- **RedisJSON**: Module to store, update, and query JSON documents natively.
- **RediSearch**: Secondary indexing and querying engine supporting full-text search, numeric, tag, geo filters.
- Combined power: Flexible document model + advanced query capability.

---

# Slide 4: SQL Entity Design - User, Portfolio, Transactions

- **Users** table
  - id, name, email
- **Portfolio** table
  - user_id, stock, quantity, gain/loss
- **Transactions** table
  - user_id, txn_id, type, amount, timestamp

---

# Slide 5: Challenges in SQL Model at Scale

- Complex JOINs across tables.
- Slower queries with increasing users and transactions.
- Multiple queries needed to retrieve full user context.
- Difficult to scale horizontally.

---

# Slide 6: RedisJSON Document Model

```json
{
  "userId": "u1",
  "name": "User 1",
  "portfolio": [
    {"stock": "AAPL", "quantity": 10, "gainLoss": 15.5},
    {"stock": "TSLA", "quantity": 5, "gainLoss": -3.2}
  ],
  "transactions": [
    {"txnId": "t1", "type": "BUY", "amount": 2000, "timestamp": "2024-01-01T10:00:00Z"},
    {"txnId": "t2", "type": "SELL", "amount": 3000, "timestamp": "2024-01-03T10:00:00Z"}
  ]
}
```

---

# Slide 7: RediSearch Index and Query Examples

- **Index Definition**:
  - `@userId`, `@portfolio[*].stock`, `@portfolio[*].gainLoss`, `@transactions[*].timestamp`

- **Search Query**:
  - List user portfolio by userId ordered by gain/loss:
    ```
    FT.SEARCH idx:users "@userId:{u1}" SORTBY gainLoss DESC
    ```

  - List recent transactions by userId ordered by timestamp:
    ```
    FT.SEARCH idx:users "@userId:{u1}" SORTBY timestamp DESC
    ```

---

# Slide 8: What is a Vector Database?

- A database for storing high-dimensional vectors.
- Supports KNN (k-nearest neighbors) search using cosine, Euclidean, IP distance.
- Used in AI/ML, recommendation, semantic search, NLP.

---

# Slide 9: Redis Vector DB vs Others

| Feature         | Redis Vector DB | FAISS | Pinecone | Weaviate |
|-----------------|-----------------|-------|----------|----------|
| In-memory speed | ✅              | ✅     | ❌        | ❌        |
| Text + vector   | ✅ (RediSearch) | ❌     | ✅        | ✅        |
| JSON support    | ✅ (RedisJSON)  | ❌     | ✅        | ✅        |
| Built-in HA     | ✅              | ❌     | ✅        | ✅        |

---

# Slide 10: RedisVL Library Features

- Simplified vector schema and indexing
- Built on top of RedisJSON + RediSearch
- Native client for insert/query/knn operations
- Zero-config integration with your app