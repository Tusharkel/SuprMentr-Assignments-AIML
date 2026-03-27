'''
*Assignment (03/03/2026)*

*Assignment Name* : Build Your First Dataset
*Description* : Create a dataset (e.g., study hours vs marks), identify features & labels, predict relationship.
'''

import pandas as pd
data = {
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "marks": [35, 40, 50, 55, 65, 70, 80, 88, 95]
}
df = pd.DataFrame(data)
X = df[["study_hours"]]   
y = df["marks"]           
print("Dataset:\n")
print(df)
print("\nFeature (Input):")
print(X.head())
print("\nLabel (Output):")
print(y.head())
correlation = df["study_hours"].corr(df["marks"])
print("\nRelationship between study hours and marks:", correlation)