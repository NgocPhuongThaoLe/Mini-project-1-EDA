import pandas as pd
import numpy as np

# 1. Read data file 
file_path = r"C:\Users\thaol\OneDrive\Documents\GitHub\Mini-project-1-EDA\1. data\raw\churn_prediction.csv"
df_churn_predictions = pd.read_csv(file_path)

print("initial shape:", df_churn_predictions.shape)

# 2. Handle duplicates
# Based on EDA results, the number of duplicate rows is 0, but this step is still included to standardize the workflow
df = df.drop_duplicates() 