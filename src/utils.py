import sys
import os
import pandas as pd
import numpy as np
import dill as pickle
from sklearn.metrics import r2_score  
from src.exception import CustomException  
 

def save_object(file_path, obj):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'wb') as file_obj:
     pickle.dump(obj, file_obj)
        
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            print(f'Model Name: {model}')
            # Train model
            model.fit(X_train, y_train)

            # Predict Testing data
            y_test_pred = model.predict(X_test)

            # Get R2 scores
            test_model_score = r2_score(y_test, y_test_pred)
            print(f'R2 score: {test_model_score}')

            report[list(models.keys())[i]] = test_model_score
        return report  
    except Exception as e:
        raise CustomException(e, sys) 

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)