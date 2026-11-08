import pandas as pd
import sqlite3

conn = sqlite3.connect('data/bank_transactions.db')
query = """
SELECT
     client_id,
     transaction_date,
     amount,
     LEAD(transaction_date) OVER (
        PARTITION BY client_id 
        ORDER BY transaction_date ASC
    ) as next_transaction_date
FROM transactions;
"""

df = pd.read_sql_query(query, conn)
print(df)
conn.close()