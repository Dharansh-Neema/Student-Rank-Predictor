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
visuals_dir = "./analytics/visuals" 
os.makedirs(analytics_dir,exist_ok=True)
os.makedirs(visuals_dir,exist_ok=True)


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

def data_visualization(file_name:str)->None:
    """This function visualise the data and 
        plot it using matplotlib and save it on analytics folder"""
    file_path = os.path.join(data_dir,file_name)
    try:
        df = pd.read_csv(file_path)
        sns.set(style="whitegrid")
        # 1. Scatter Plot: Score vs Accuracy
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df["score"], y=df["accuracy"], hue=df["rank"], palette="coolwarm")
        plt.title("Score vs Accuracy (Colored by Rank)")
        plt.xlabel("Score")
        plt.ylabel("Accuracy")
        plt.savefig(os.path.join(visuals_dir, "score_vs_accuracy.png"))
        plt.close()

        # 2. Scatter Plot: Score vs Correct Answers ###
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df["score"], y=df["correct_answers"], hue=df["rank"], palette="viridis")
        plt.title("Score vs Correct Answers (Colored by Rank)")
        plt.xlabel("Score")
        plt.ylabel("Correct Answers")
        plt.savefig(os.path.join(visuals_dir, "score_vs_correct_answers.png"))
        plt.close()

        # 3. Line Plot: Accuracy vs Rank ###
        plt.figure(figsize=(8, 5))
        sns.lineplot(x=df["rank"], y=df["accuracy"], marker="o", color="green")
        plt.title("Accuracy vs Rank")
        plt.xlabel("Rank")
        plt.ylabel("Accuracy")
        plt.savefig(os.path.join(visuals_dir, "accuracy_vs_rank.png"))
        plt.close()
        
        logger.debug(f"All the visuals are save to {visuals_dir} succesfully.")

    except Exception as e:
        logger.error("Unexpected error occured",e)
        raise

if __name__ == "__main__":
    file_name = "previous_year_data.csv"
    data_analysis(file_name)
    data_visualization(file_name)