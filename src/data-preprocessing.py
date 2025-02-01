import pandas as pd
import os 
from src.logger import setup_logger

logger = setup_logger(name="data-preprocessing",log_file="logs/data-preprocessing.log",console_level="DEBUG")
import os
import pandas as pd
import re

def pre_process_previous_year_data(data_file_path: str) -> None:
    """ 
    This function pre-processes the previous year data for quiz submission and saves it into a new directory 
    of processed data
    """
    data_dir = "./data/processed/"
    file_name = "previous_year_data.csv"

    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, file_name)
    
    try:
        df = pd.read_csv(data_file_path)

        # Drop the non-required columns
        new_df = df.drop(columns=['id', 'quiz_id', 'user_id', 'submitted_at', 'created_at', 'updated_at', 'source', 'type', 'started_at', 'ended_at', 'duration', 'response_map', 'quiz'])
        
        # Extract only the rank from 'rank_text' column
        new_df['rank'] = new_df['rank_text'].str.extract('(\d+)').astype(int)
        new_df = new_df.drop(columns=['rank_text'])
        
        # Removing % from accuracy
        new_df['accuracy'] = new_df['accuracy'].str.replace('%','').astype(float)
        new_df = new_df.apply(pd.to_numeric)
        logger.debug("Successfully processed previous year data")
        
        # Saving the file to the desired location
        new_df.to_csv(file_path, index=False)
        logger.debug("Saved the processed data at desired location")

    except Exception as e:
        logger.error("Unexpected error occurred while pre-processing the previous year data", exc_info=True)
        raise


def pre_process_quiz_data(file_path:str)->None:
    """
    This function pre-process the quiz submission data and save to processed directory.
    """
    data_dir = "./data/processed/"
    file_name = "quiz_submission.csv"
    os.makedirs(data_dir,exist_ok=True)
    file_loc=os.path.join(data_dir,file_name)
    try:
        df = pd.read_csv(file_path)
        new_df = df.drop(columns=["id","quiz_id","user_id","submitted_at","created_at","updated_at","type","started_at","ended_at","duration","response_map","rank_text","source"])
        new_df['accuracy'] = new_df['accuracy'].str.replace('%','').astype(float)
        new_df = new_df.apply(pd.to_numeric)
        logger.debug("Successfully processed quiz submission data")

        # Saving the file 
        new_df.to_csv(file_loc,index=False)
        logger.debug("Saving the data to desired location")

    except Exception as e:
        logger.error("Unexpected Error occured while pre-processing the quiz submission data",e)
        raise


if __name__ == "__main__":
    path_prv = "./data/csv/previous_year_data.csv"
    path_quiz = "./data/csv/quiz_submission_data.csv"
    pre_process_previous_year_data(path_prv)
    pre_process_quiz_data(path_quiz)

