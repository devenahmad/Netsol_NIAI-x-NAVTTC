# Task 53 - decision tree classifier
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

tree = DecisionTreeClassifier(random_state=1)
tree.fit(X_train, y_train)
print("full tree  train:", round(tree.score(X_train, y_train), 3), " test:", round(tree.score(X_test, y_test), 3))

small = DecisionTreeClassifier(max_depth=3, random_state=1)
small.fit(X_train, y_train)
pred = small.predict(X_test)
print("depth 3    train:", round(small.score(X_train, y_train), 3), " test:", round(accuracy_score(y_test, pred), 3))
print(confusion_matrix(y_test, pred))

for name, imp in zip(iris.feature_names, small.feature_importances_):
    print(f"{name:20s} {imp:.2f}")

print()
print(export_text(small, feature_names=iris.feature_names))

print("depth vs test accuracy")
for d in range(1, 8):
    t = DecisionTreeClassifier(max_depth=d, random_state=1).fit(X_train, y_train)
    print(d, round(t.score(X_test, y_test), 3))

plt.figure(figsize=(12, 7))
plot_tree(small, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.savefig("task_53_tree.png")
print("tree picture saved as task_53_tree.png")