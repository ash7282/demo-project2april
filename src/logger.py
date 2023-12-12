import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

from src.exception import CustomeException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedir(dir_path,exit_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dumpl(obj,fil_obj)


    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}

        for i in rang(len(models)):
            model=list(models.values())[i]
            #tarin model
            model.fit(X_train,y_train)




            #predic testing data

            y_test_pred = model.predict(X_test)

            test_model_score=r2_score(y_test,y_test_pred)

            report[list(model.keys())[i]]=test_model_score

        return report
    
    except Exception as e:
        logging.info('Exception occure during model training')

        raise CustomException(e,sys)