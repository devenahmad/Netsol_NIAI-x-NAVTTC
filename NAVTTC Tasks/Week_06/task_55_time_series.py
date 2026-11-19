# Task 55 - time series analysis with pandas
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(5)
dates = pd.date_range("2022-01-01", "2023-12-31", freq="D")

# slow upward trend + yearly wave (winter high) + weekend dip + noise
trend = np.linspace(1000, 1200, len(dates))
season = 150 * np.cos(2 * np.pi * (dates.dayofyear - 15) / 365)
weekend = np.where(dates.dayofweek >= 5, -80, 0)
noise = np.random.normal(0, 30, len(dates))

df = pd.DataFrame({"usage": trend + season + weekend + noise}, index=dates)
df.index.name = "date"
print(df.head())

df["year"] = df.index.year
df["month"] = df.index.month
df["weekday"] = df.index.day_name()

print("\nsingle day:", round(df.loc["2022-07-04", "usage"], 1))
print("\nJune 2023 average:", round(df.loc["2023-06", "usage"].mean(), 1))

print("\naverage usage by weekday")
print(df.groupby("weekday")["usage"].mean().round(0).sort_values())

weekly = df["usage"].resample("W").mean()
monthly = df["usage"].resample("MS").mean()
print("\nmonthly")
print(monthly.head(6).round(0))

df["rolling_7"] = df["usage"].rolling(7).mean()
df["rolling_30"] = df["usage"].rolling(30).mean()

df["diff_1"] = df["usage"].diff()
df["yoy"] = df["usage"].pct_change(365) * 100
print("\nyear on year change, last row: %.1f%%" % df["yoy"].iloc[-1])

# very simple forecast: same day last year + yearly growth
last_year = df["usage"].iloc[-365:].values
growth = df["usage"].iloc[-365:].mean() / df["usage"].iloc[-730:-365].mean()
forecast = last_year[:7] * growth
print("next 7 days forecast:", forecast.round(0))

fig, ax = plt.subplots(2, 1, figsize=(10, 7))
df["usage"].plot(ax=ax[0], alpha=0.4, label="daily")
df["rolling_30"].plot(ax=ax[0], color="red", label="30 day average")
ax[0].legend()
monthly.plot(ax=ax[1], marker="o")
ax[1].set_title("monthly average")
plt.tight_layout()
plt.savefig("task_55_timeseries.png")
print("plot saved as task_55_timeseries.png")