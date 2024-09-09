from exception import CustomException
from logger import logging
import pandas as pd
import sqlite3
import pandas as pd




# Create a connection to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('my_database.db')


df=pd.read_csv("Artifacts/train.csv")
# print(df)

df.to_sql("my_table",conn,if_exists="replace",index=False)


db_from_db=pd.read_sql("Select * from my_table",conn)

print(db_from_db)
