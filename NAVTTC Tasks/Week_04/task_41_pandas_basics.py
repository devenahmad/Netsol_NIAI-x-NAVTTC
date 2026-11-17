# Task 41 - pandas basics
import pandas as pd

data = {
    "name": ["ali", "sara", "bilal", "hina"],
    "age": [21, 23, 22, 24],
    "city": ["lahore", "karachi", "lahore", "multan"],
}
df = pd.DataFrame(data)
print(df)

print("\nversion:", pd.__version__)
print("\nshape:", df.shape)
print("\ncolumns:", list(df.columns))

print("\n", df["name"])

print("\n", df[df["age"] > 21])
print("\n", df[df["city"] == "lahore"])

df["age_next_year"] = df["age"] + 1
print("\n", df)

print("\naverage age:", df["age"].mean())
print("oldest:", df.loc[df["age"].idxmax(), "name"])

print("\n", df.sort_values("age", ascending=False))