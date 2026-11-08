import pandas as pd
import sqlite3

conn = sqlite3.connect('data/bank_transactions.db')
data = {
    'client_id': [1, 1, 1, 1, 2, 2, 3],
    'transaction_date': [
        '2023-10-01', '2023-10-05', '2023-10-10', '2023-10-15',
        '2023-10-02', '2023-10-08',
        '2023-10-03'
    ],
    'amount': [150.0, 50.0, 200.0, 10.0, 300.0, 500.0, 120.0]
}

df = pd.DataFrame(data)
df.to_sql('transactions',conn,if_exists='replace', index=False)
print("done")
conn.close()