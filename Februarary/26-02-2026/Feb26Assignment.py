'''
*Assignment (26/02/2026)*

*Assignment Name* : Data Doctor
*Description* : Clean a dataset by handling missing values, removing duplicates, standardizing text, and explain why cleaning matters.
'''

import pandas as pd
data = {
    "Name": ["Alice", "Bob", "alice", "Charlie", None],
    "StudyHours": [5, 7, 5, None, 8],
    "Marks": [60, 70, 60, 75, 80]
}
df = pd.DataFrame(data)
print("Original Dataset:\n")
print(df)
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
df["Name"] = df["Name"].fillna("Unknown")
df["Name"] = df["Name"].str.lower()
df = df.drop_duplicates()
print("\nCleaned Dataset:\n")
print(df)