import os
import sqlite3

import pandas as pd

os.makedirs("db", exist_ok=True)

db_path = "db/real_estate.db"

if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)

conn.execute("PRAGMA foreign_keys = OFF;")


def load_tb(table: str):
    df = pd.read_csv(f"data/{table}.csv")
    df.to_sql(table, conn, if_exists="append", index=False)


load_tb("location")
load_tb("agent")
load_tb("buyer")
load_tb("property")
load_tb("property_feature")
load_tb("transactions")
load_tb("purchase")
load_tb("valuation")

conn.execute("PRAGMA foreign_keys = ON;")

conn.commit()

conn.close()
