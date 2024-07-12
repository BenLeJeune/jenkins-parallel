"""
This script is the final script to be executed, after the parallel jobs have finished running.
This will collect all the data saved by the parallel jobs, and output the combined dataframe.
"""
import pandas as pd
import os

files = os.listdir('tmp/')
dfs = []
for path in files:
    df = pd.read_csv('tmp/' + path, index_col=0)
    print(df)
    dfs.append(df)

combined_df = pd.concat(dfs)

print("Final output reached!")
print(combined_df)