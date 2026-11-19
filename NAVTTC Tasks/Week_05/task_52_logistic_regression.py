# Task 52 - logistic regression
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_digits

# part 1: binary
np.random.seed(3)
hours = np.random.uniform(0, 10, 200)
chance = 1 / (1 + np.exp(-(hours - 5)))
passed = (np.random.rand(200) < chance).astype(int)

X = hours.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, passed, test_size=0.25, random_state=1)

clf = LogisticRegression()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

print("binary accuracy:", round(accuracy_score(y_test, pred), 3))
print("confusion matrix:")
print(confusion_matrix(y_test, pred))

for h in (2, 5, 8):
    p = clf.predict_proba([[h]])[0][1]
    print(f"{h} hours of study -> {p * 100:.0f}% chance of passing")

# part 2: digits
digits = load_digits()
print("\ndigits data shape:", digits.data.shape)

X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.25, random_state=2
)

clf2 = LogisticRegression(max_iter=3000)
clf2.fit(X_train, y_train)
pred2 = clf2.predict(X_test)

print("digits accuracy:", round(accuracy_score(y_test, pred2), 3))
print(classification_report(y_test, pred2))

wrong = np.where(pred2 != y_test)[0]
print("mistakes:", len(wrong))
for i in wrong[:5]:
    print("  real", y_test[i], "predicted", pred2[i])