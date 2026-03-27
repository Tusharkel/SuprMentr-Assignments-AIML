'''
Assignment (24/02/2026)

Assignment Name : Dataset Detective
Description : Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.
'''

import pandas as pd
df = pd.read_csv("data.csv")
print("Top 5 Rows:")
print(df.head())
highest_column = df.mean(numeric_only=True).idxmax()
print("\nColumn with Highest Average Value:", highest_column)
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
print("\nTotal Missing Values:", df.isnull().sum().sum())