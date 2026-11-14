# Task 44 - pandas dataframes
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0])
print(df.loc[[0, 1]])

df2 = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df2)
print(df2.loc["day2"])

print(df2.iloc[0])
print(df2.iloc[0:2, 0])

df2["ratio"] = df2["calories"] / df2["duration"]
print(df2)
df2 = df2.drop(columns=["ratio"])

new_row = pd.DataFrame({"calories": [500], "duration": [60]}, index=["day4"])
df2 = pd.concat([df2, new_row])
print(df2)

df2 = df2.rename(columns={"calories": "cal"})
print(df2)

print(df2.info())
print(df2.T)