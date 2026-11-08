import sqlite3
import pandas as pd

conn = sqlite3.connect('data/bank_transactions.db')
query = """
SELECT
     client_id,
     transaction_date,
     amount,
     LAG(transaction_date) OVER (
        PARTITION BY client_id 
        ORDER BY transaction_date ASC
    ) as prev_transaction_date
FROM transactions;
"""
df = pd.read_sql_query(query, conn)
print(df)
conn.close()
