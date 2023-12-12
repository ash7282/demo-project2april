import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_trasformation import DataTransformation


## Initialize the Data Ingestion Configuration
## real-time and batch Real-time data ingestion is when data is ingested as it occurs, and batch data ingestion is when the information is collected over time and then processed at once.
    
@dataclass 
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    ##OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. 
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')


## create a class for Data Ingestion

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initialize_data_ingestion(self):
        logging.info('Data Ingestion Methods Starts')
        try:
            df.pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')
##This module defines functions and classes which implement a flexible event logging system for applications and libraries.
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exit_ok=True)
            ##Then os.makedirs() method will create all unavailable/missing directory in the specified path.
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        
        except Exception as e:
            logging.info('Exception occured at data Ingestion stage')
            raise CustomeException(e,sys)
        