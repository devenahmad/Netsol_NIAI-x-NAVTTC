# Task 45 - reading and writing csv files with pandas
import pandas as pd

df = pd.DataFrame({
    "name": ["ali", "sara", "bilal", "hina", "omar"],
    "marks": [78, 91, 65, 88, 54],
    "grade": ["B", "A", "C", "B", "D"],
})
df.to_csv("students.csv", index=False)
print("saved students.csv")

data = pd.read_csv("students.csv")
print(data)

print(data.head(2))
print(data.tail(2))

print(data.shape)
print(data.dtypes)

print(data.to_string())

print(pd.read_csv("students.csv", usecols=["name", "marks"]))

print(pd.read_csv("students.csv", nrows=3))

print(pd.read_csv("students.csv", index_col="name"))

data[data["marks"] > 70].to_csv("top_students.csv", index=False)
print(pd.read_csv("top_students.csv"))