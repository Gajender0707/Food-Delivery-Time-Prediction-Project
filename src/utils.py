from exception import CustomException
from logger import logging
import pandas as pd
import sqlite3
import pandas as pd
import os 


# Create a connection to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('my_database.db')

class data_from_db:

    def __init__(self,row_data_path):
        self.row_data_path=row_data_path


    def data_store(self):
        df=pd.read_csv(self.row_data_path)
        # print(df)
        df.to_sql("training_data",conn,if_exists="append",index=False)




    def data(self):
        pass


if __name__=="__main__":
    obj=data_from_db("data/train.csv")
    obj.data_store()
