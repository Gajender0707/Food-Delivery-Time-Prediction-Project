import os 
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class dataingestion_config:
    data_path=os.path.join("Artifacts","data.csv")
    training_data_path=os.path.join("artifacts","train.csv")
    testing_data_path=os.path.join("Artifacts","test.csv")



# a=dataingestion_config
# print(a.data_path)
class data_ingestion:
    def __init__(self,raw_data_path):
        self.data_ingestion_config=dataingestion_config()
        self.raw_data_path=raw_data_path


    def initiate_data_ingestion(self):
        raw_data=pd.read_csv(self.raw_data_path)
        from sklearn.model_selection import train_test_split
        print(self.data_ingestion_config.data_path)
        print(self.data_ingestion_config.training_data_path)
        # Assuming X is your feature matrix and y is your target variable
        train_data,test_data= train_test_split(raw_data, test_size=0.2, random_state=42)
        # print(train_data)
        # print(test_data)
        # print(type(train_data))
        # print(train_data.head(1))
        # train_data.to_csv(self.data_ingestion_config.data_path)
        # print(type(self.data_ingestion_config.training_data_path))
        # os.makedirs(os.path.join(self.data_ingestion_config.data_path))
        train_data.to_csv(self.data_ingestion_config.training_data_path)
        test_data.to_csv(self.data_ingestion_config.testing_data_path)

if __name__=="__main__":
    r_d_p="/Users/sanju/Documents/DS/ML /ML Projects/Food Delivery Time Prediction End to End Project/data/train.csv"
    res=data_ingestion(r_d_p)
    # print(res.initiate_data_ingestion())






