import os
import pickle
import pandas as pd
from src.logger import setup_logger

logger = setup_logger(name="model-testing",log_file="logs/model-testing.log",console_level="DEBUG")

data_dir = "./data/processed"
model_dir ="./model/"
def load_model(path:str):
    """Load the model from desired location"""
    try:
        model_path = os.path.join(model_dir,path)
        with open(model_path,"rb") as file:
            model=pickle.load(file)
        logger.debug("Model is loaded from the deaired location")
        return model
        
    except Exception as e:
        logger.error("Unexpected error occurred",e)
        raise

def test_model(file_path):
    """ This function with the help of trained model predict a rank with a given dataset """
    data_file_name = os.path.join(data_dir,file_path)
    try:
        df = pd.read_csv(data_file_name)
        model = load_model("model.pkl")
        logger.debug("Model loaded successfully")
        predict_res = model.predict(df)
        print(predict_res)
        logger.debug("Prediction completed")
        return predict_res.round()
        

    except Exception as e:
        logger.error("Some error occurred while predicting the rank",e)
        raise
if __name__=='__main__':
    
    try:
        path = "quiz_submission.csv"
        rank=test_model(path)
        print(rank)
    except Exception as e:
        logger.error("Unexpected error ",e)
        raise