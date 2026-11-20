# Task 58 - feed forward neural network class (numpy only)
# a small reusable network where you can stack as many layers as you like
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


class FeedForward:
    def __init__(self, sizes, lr=0.1, seed=0):
        rng = np.random.RandomState(seed)
        self.lr = lr
        self.W = [rng.randn(a, b) * np.sqrt(2 / a) for a, b in zip(sizes[:-1], sizes[1:])]
        self.b = [np.zeros((1, b)) for b in sizes[1:]]

    def _relu(self, z):
        return np.maximum(0, z)

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def forward(self, X):
        self.acts = [X]
        a = X
        for i in range(len(self.W) - 1):
            a = self._relu(a @ self.W[i] + self.b[i])
            self.acts.append(a)
        a = self._sigmoid(a @ self.W[-1] + self.b[-1])
        self.acts.append(a)
        return a

    def backward(self, y):
        n = len(y)
        delta = self.acts[-1] - y
        for i in reversed(range(len(self.W))):
            dW = self.acts[i].T @ delta / n
            db = delta.mean(axis=0, keepdims=True)
            if i > 0:
                delta = (delta @ self.W[i].T) * (self.acts[i] > 0)
            self.W[i] -= self.lr * dW
            self.b[i] -= self.lr * db

    def fit(self, X, y, epochs=2000, show_every=500):
        y = y.reshape(-1, 1)
        for e in range(epochs + 1):
            p = self.forward(X)
            self.backward(y)
            if e % show_every == 0:
                p = np.clip(p, 1e-9, 1 - 1e-9)
                loss = -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
                print(f"epoch {e:5d}  loss {loss:.4f}")

    def predict(self, X):
        return (self.forward(X) > 0.5).astype(int).ravel()


X, y = make_moons(600, noise=0.2, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

net = FeedForward([2, 16, 16, 1], lr=0.2)
net.fit(X_train, y_train)

print("\ntrain accuracy:", round((net.predict(X_train) == y_train).mean(), 3))
print("test accuracy :", round((net.predict(X_test) == y_test).mean(), 3))