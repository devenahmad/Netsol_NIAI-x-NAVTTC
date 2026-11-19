# Task 51 - linear regression with scikit-learn
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")      # Anti-Grain Geometry -> lets it save the plot without a window, Non-GUI
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(7)
hours = np.random.uniform(1, 10, 80)
marks = 8 * hours + 15 + np.random.normal(0, 6, 80)
df = pd.DataFrame({"hours": hours, "marks": marks})
print(df.head())

X = df[["hours"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nslope    :", round(model.coef_[0], 2), "(real answer was 8)")
print("intercept:", round(model.intercept_, 2), "(real answer was 15)")

pred = model.predict(X_test)
print("\nMAE :", round(mean_absolute_error(y_test, pred), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, pred)), 2))
print("R2  :", round(r2_score(y_test, pred), 3))

print("\n6.5 hours of study ->", round(model.predict(pd.DataFrame({"hours": [6.5]}))[0], 1), "marks")

plt.scatter(X_test, y_test, label="real")
plt.plot(X_test.sort_values("hours"), model.predict(X_test.sort_values("hours")), color="red", label="model")
plt.xlabel("hours studied")
plt.ylabel("marks")
plt.legend()
plt.savefig("task_51_plot.png")
print("plot saved as task_51_plot.png")