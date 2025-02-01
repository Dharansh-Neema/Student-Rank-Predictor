import pandas as pd
from src.logger import setup_logger 
import os 
import requests
import json

# logger setup
logger = setup_logger(
    log_file="logs/data-ingestion.log",
    console_level="DEBUG",
    file_level="DEBUG"
)

def inject_data(url:str,file_name)->str:
    # directory to save data
    data_dir = "./data/json/"
    os.makedirs(data_dir,exist_ok=True)
    try:
        response = requests.get(url)
        
        data = response.json()
        file_path = os.path.join(data_dir,f"{file_name}.json")
        
        with open(file_path,"w") as file:
            json.dump(data,file,indent=4)

        logger.debug(f"Data saved successfully at :{file_path}")
        return file_path
    except Exception as e:
        logger.error(f"Unexpected error occurred while fetching json data: {e}")
        raise


def convert_data_csv(data_path:str,file_name:str)->None:
    data_dir = "./data/csv"
    os.makedirs(data_dir,exist_ok=True)

    try:
        df = pd.read_json(data_path)
        file_path = os.path.join(data_dir,f"{file_name}.csv")
        df.to_csv(file_path,index=False)
        logger.debug("Converted json file to json")

    except Exception as e:
        logger.error(f"Unexpected error occured while converting json data to csv {e}")
        raise
if __name__ == "__main__":
    
    previous_year_data_url = "https://api.jsonserve.com/XgAgFJ"
    prv_year_data_path = inject_data(previous_year_data_url,"previous_year_data")
    convert_data_csv(prv_year_data_path,"previous_year_data")

    # quiz_submission_url = "https://api.jsonserve.com/rJvd7g"
    # quiz_submission_data_path = inject_data(quiz_submission_url,"quiz_submission_data")
    convert_data_csv("./data/json/quiz_submission_data.json","quiz_submission_data") 


