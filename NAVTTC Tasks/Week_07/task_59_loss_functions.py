# Task 59 - loss functions written by hand
import numpy as np

# for predicting numbers (regression)
y_true = np.array([3.0, 5.0, 2.5, 7.0, 4.0])
y_pred = np.array([2.5, 5.0, 4.0, 8.0, 3.0])


def mse(y, p):
    return np.mean((y - p) ** 2)


def rmse(y, p):
    return np.sqrt(mse(y, p))


def mae(y, p):
    return np.mean(np.abs(y - p))


def huber(y, p, delta=1.0):
    err = y - p
    small = np.abs(err) <= delta
    return np.mean(np.where(small, 0.5 * err ** 2, delta * (np.abs(err) - 0.5 * delta)))


def log_cosh(y, p):
    return np.mean(np.log(np.cosh(p - y)))


print("regression")
print("  MSE      :", round(mse(y_true, y_pred), 4))
print("  RMSE     :", round(rmse(y_true, y_pred), 4))
print("  MAE      :", round(mae(y_true, y_pred), 4))
print("  Huber    :", round(huber(y_true, y_pred), 4))
print("  Log-cosh :", round(log_cosh(y_true, y_pred), 4))

bad = y_pred.copy()
bad[0] = 30
print("\nwith one terrible prediction")
print("  MSE  :", round(mse(y_true, bad), 2), "(explodes)")
print("  MAE  :", round(mae(y_true, bad), 2), "(grows slowly)")
print("  Huber:", round(huber(y_true, bad), 2))

# for yes/no (binary classification)
labels = np.array([1, 0, 1, 1, 0])
probs = np.array([0.9, 0.2, 0.7, 0.4, 0.1])


def binary_cross_entropy(y, p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))


def hinge(y, score):
    y = np.where(y == 0, -1, 1)       # hinge wants -1 / +1
    return np.mean(np.maximum(0, 1 - y * score))


print("\nbinary classification")
print("  cross entropy:", round(binary_cross_entropy(labels, probs), 4))
print("  hinge        :", round(hinge(labels, probs * 2 - 1), 4))

print("  sure and right (p=0.99 for a 1):", round(binary_cross_entropy(np.array([1]), np.array([0.99])), 4))
print("  sure and wrong (p=0.01 for a 1):", round(binary_cross_entropy(np.array([1]), np.array([0.01])), 4))

# many classes
def softmax(z):
    e = np.exp(z - z.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)


def categorical_cross_entropy(y_onehot, p):
    p = np.clip(p, 1e-12, 1)
    return -np.mean(np.sum(y_onehot * np.log(p), axis=1))


scores = np.array([[2.0, 1.0, 0.1], [0.5, 2.5, 0.3], [0.1, 0.2, 3.0]])
y_onehot = np.eye(3)
probs3 = softmax(scores)
print("\nmulticlass")
print("  softmax rows sum to 1:", probs3.sum(axis=1))
print("  categorical cross entropy:", round(categorical_cross_entropy(y_onehot, probs3), 4))