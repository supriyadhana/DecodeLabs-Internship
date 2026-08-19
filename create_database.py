import pandas as pd
import sqlite3

df = pd.read_csv("data/Cleaned_Dataset.csv")

connection = sqlite3.connect("data/orders.db")

df.to_sql("orders", connection, if_exists="replace", index=False)

connection.close()

print("Database created successfully!")