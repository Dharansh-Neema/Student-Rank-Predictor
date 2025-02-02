import pandas as pd
import os 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import json

#Setting up the logger
from src.logger import setup_logger
logger=setup_logger(name="data-analysis",log_file="logs/data-analysis.log",console_level="DEBUG")

#Specifiying path 
data_dir = "./data/processed/"
analytics_dir = "./analytics/"
os.makedirs(analytics_dir,exist_ok=True)


def data_analysis(file_name:str)->None:
    """
    This function do various factor data_analysis on the given dataset 
    """
    try:
        data_path = os.path.join(data_dir,file_name)
        df = pd.read_csv(data_path)
        logger.debug("Loaded the csv file to Data frame")
        analysis_result = {}

        #summary
        summary = df.describe()
        analysis_result["summary"]=summary.to_dict()

        #Correlation Matrix
        correlation_matrix = df.corr()
        analysis_result["correlation_matrix"] = correlation_matrix.to_dict()

        # Distribution Analysis
        distribution = {col: {"mean": np.mean(df[col]), "median": np.median(df[col]), "std": np.std(df[col])} for col in df.columns}
        analysis_result["distribution_analysis"] = distribution
        
        # Save Results
        summary.to_csv(os.path.join(analytics_dir, "summary.csv"))
        correlation_matrix.to_csv(os.path.join(analytics_dir, "correlation_matrix.csv"))

        with open(os.path.join(analytics_dir, "data_analysis.json"), "w") as json_file:
            json.dump(analysis_result, json_file, indent=4)
        
        logger.debug(f"Data-analysis completed and stored the result at :{analytics_dir}")


    except Exception as e:
        logger.error("Unexpected error occured while doing data analysis",e)
        raise

if __name__ == "__main__":
    file_name = "previous_year_data.csv"
    data_analysis(file_name)