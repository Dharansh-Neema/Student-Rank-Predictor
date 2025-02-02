import os
from sklearn.linear_model import LinearRegression
import json
import pandas as pd 
import numpy as np
import pickle

#Set-up logger 
from src.logger import setup_logger
logger = setup_logger(name="model-tranining",log_file="logs/model-traning.log",console_level="DEBUG")

data_dir = "./data/processed/"
model_dir = "./model/"
os.makedirs(model_dir,exist_ok=True)


def train_model(file_name:str)->LinearRegression:
    """This function will train a machine learning model using Linear
    Regression to predict the student Rank""" 
    data_path = os.path.join(data_dir,file_name)
    try:
        df = pd.read_csv(data_path)
        y_train = df["rank"]
        X_train = df.drop(columns=["rank"])
        logger.debug("Dataset loaded to dataframe and ready to train")
        model = LinearRegression()
        model.fit(X_train,y_train)
        logger.info("Model is trained and ready to use")
        return model
        
    except Exception as e:
        logger.error("Unexpected error occured while training the model",e)
        raise

def save_model(model:LinearRegression, model_file_name:str)->None:
    """
    This function save the passed model to required location in a pickle file
    """
    file_path = os.path.join(model_dir,model_file_name)
    try:
        with open(file_path,'wb') as file:
            pickle.dump(model,file)
        logger.debug(f"Model saved to {file_path}")
    
    except Exception as e:
        logger.error("Error occured while saving the model",e)
        raise
if __name__ == "__main__":
    data_file_name = "previous_year_data.csv"
    model_file_name = "model.pkl"
    
    #train the model and save it
    model = train_model(data_file_name)
    save_model(model,model_file_name)
