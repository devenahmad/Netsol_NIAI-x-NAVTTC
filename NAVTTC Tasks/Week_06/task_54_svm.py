# Task 54 - support vector machine (svm) and kernel svm
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# real data: breast cancer
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=4)

sc = StandardScaler()
X_train_s = sc.fit_transform(X_train)
X_test_s = sc.transform(X_test)

for kernel in ("linear", "poly", "rbf", "sigmoid"):
    model = SVC(kernel=kernel)
    model.fit(X_train_s, y_train)
    acc = accuracy_score(y_test, model.predict(X_test_s))
    print(f"{kernel:8s} accuracy: {acc:.3f}")

best = SVC(kernel="rbf", C=1.0, gamma="scale").fit(X_train_s, y_train)
pred = best.predict(X_test_s)
print("\nrbf kernel details")
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, target_names=data.target_names))

# why kernels -> handle curved data
Xm, ym = make_moons(300, noise=0.2, random_state=0)
lin = SVC(kernel="linear").fit(Xm, ym)
rbf = SVC(kernel="rbf").fit(Xm, ym)
print("moons data -> linear:", round(lin.score(Xm, ym), 3), " rbf:", round(rbf.score(Xm, ym), 3))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
xx, yy = np.meshgrid(np.linspace(-2, 3, 200), np.linspace(-1.5, 2, 200))
for ax, m, title in zip(axes, (lin, rbf), ("linear", "rbf")):
    zz = m.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, zz, alpha=0.3)
    ax.scatter(Xm[:, 0], Xm[:, 1], c=ym, edgecolor="k", s=15)
    ax.set_title(title)
plt.savefig("task_54_svm.png")
print("plot saved as task_54_svm.png")