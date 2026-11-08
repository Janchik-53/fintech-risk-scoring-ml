import sqlite3
import pandas as pd

conn = sqlite3.connect('data/bank_transactions.db')

query = """
SELECT 
    client_id,
    transaction_date,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY client_id 
        ORDER BY transaction_date DESC
    ) as recent_rank
FROM transactions;
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()