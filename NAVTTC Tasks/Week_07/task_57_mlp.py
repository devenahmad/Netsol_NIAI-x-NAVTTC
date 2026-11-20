# Task 57 - multi layer perceptron (mlp) using scikit-learn
import numpy as np
from sklearn.datasets import load_digits, make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# curved data
X, y = make_moons(500, noise=0.25, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

mlp = MLPClassifier(hidden_layer_sizes=(16, 8), activation="relu", max_iter=2000, random_state=0)
mlp.fit(X_train, y_train)
print("moons accuracy:", round(mlp.score(X_test, y_test), 3))
print("layers:", [w.shape for w in mlp.coefs_])

# handwritten digits
d = load_digits()
X_train, X_test, y_train, y_test = train_test_split(d.data, d.target, test_size=0.25, random_state=1)

sc = StandardScaler().fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

for sizes in [(10,), (50,), (100, 50)]:
    m = MLPClassifier(hidden_layer_sizes=sizes, max_iter=500, random_state=1)
    m.fit(X_train, y_train)
    print(f"hidden {str(sizes):10s} -> test accuracy {m.score(X_test, y_test):.3f}")

for act in ("relu", "tanh", "logistic"):
    m = MLPClassifier(hidden_layer_sizes=(50,), activation=act, max_iter=500, random_state=1)
    m.fit(X_train, y_train)
    print(f"activation {act:9s} -> test accuracy {m.score(X_test, y_test):.3f}")

best = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=1).fit(X_train, y_train)
pred = best.predict(X_test)
print("\nconfusion matrix")
print(confusion_matrix(y_test, pred))
print("loss at the end:", round(best.loss_, 4), "after", best.n_iter_, "rounds")