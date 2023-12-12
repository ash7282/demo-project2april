import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.exception import CustomeException

from src.logger import logging
import os

from src.utils import save_object]

@dataclass

class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pk1')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


    def get_data_transformation_object(self):

        try:
            logging.info('Data Transformation initiated')
            #Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols= ['carat','depth','table','X','y','z']


            # Define the custom ranking for each original variable
            cut_categories = ['Fair','Good ','Very Good','Premium','Ideal']
            color_categories =['D','E','F','G','H','I','J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']


            logging.info('Pipeline Initiated')


            ##Numerical Pipeline

            num_pipeline=Pipeline(
                steps=[
                ('inputer',SimpleImputer(strategy='median')),
                ('Scaler',StandardScalar)
                ]
            )

            #categories Pipeline
            cat_pipeline=Pipeline(
                steps=[
                 ('imputer',SimpleImputer(stratergy='most_frequent')),
                 ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                 ('Scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            return preprocessor
        
        logging.info('pipeline completed')

    except Exception as e:
        logging.info('Error in data Transformation')
    
        raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            #reading train and test data

            train_df = pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Read train and test data comleted')
            logging.info(f"train Dataframe Head :\n {train_df.head().to_string()}")
            logging.infor(f'Test DataFrame head :\n {test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')
             
            preprocessing_obj=self.get_data_transformation_object()
            
            target_column_name ='Price'
            drop_columns =[target_column_name,'id']

            input_feature_train_df = train_df.drop(columns=drop_columns,axix=1)
            target_feature_train_df = train_df[taget_columns_name]

            input_feature_train_df=train_df.drop(column=drop_column,axis=1)
            target_feature_test_df=test_df[target_column_name]

            ##transformating using preprocessor obj

            input_feature_train_arr=preprocessor_obj.fi_transformation(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transformation(inpute_feature_test_df)
       
            logging.info("Applying preprocessing object on training and testing datasets")


            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr =np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(

                file_path=self.data_transformation_config.preprocessing_obj_file_path,
                obj=preprocessing_obj

            )

            logging.info('Preprocessing pickel file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_cofig.preprocessor_obj_file_path,

            )
        
        except Exception as e:
            logging.info('Exception occure in the initiate_datatransformation')

            raise CustomException(e.sys)