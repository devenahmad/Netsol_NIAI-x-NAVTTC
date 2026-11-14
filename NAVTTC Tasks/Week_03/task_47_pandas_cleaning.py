# Task 47 - cleaning messy data with pandas
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "name": ["ali", "sara", None, "bilal", "sara", "hina", "omar"],
    "age": [21, 23, 25, np.nan, 23, 250, 22],
    "city": ["lahore", "Karachi", "lahore", "LAHORE", "Karachi", "multan", None],
    "joined": ["2023-01-05", "2023-02-10", "not a date", "2023-03-15", "2023-02-10", "2023-04-01", "2023-05-20"],
})
print("original")
print(df)

print("\nmissing per column")
print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("unknown")
df = df.dropna(subset=["name"])

print("\nduplicates:", df.duplicated().sum())
df = df.drop_duplicates()

df["city"] = df["city"].str.lower().str.strip()

df["joined"] = pd.to_datetime(df["joined"], errors="coerce")

df.loc[df["age"] > 100, "age"] = df["age"].median()

df["age"] = df["age"].astype(int)

print("\ncleaned")
print(df)
print(df.dtypes)