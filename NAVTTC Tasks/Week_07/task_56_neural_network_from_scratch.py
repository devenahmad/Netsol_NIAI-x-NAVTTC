# Task 56 - neural network from scratch (only numpy)
import numpy as np

np.random.seed(1)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def sigmoid_slope(a):
    return a * (1 - a)


W1 = np.random.randn(2, 4)
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1)
b2 = np.zeros((1, 1))

lr = 0.5

for epoch in range(10001):
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)

    loss = np.mean((y - out) ** 2)

    d_out = (out - y) * sigmoid_slope(out)
    d_W2 = h.T @ d_out
    d_b2 = d_out.sum(axis=0, keepdims=True)

    d_h = d_out @ W2.T * sigmoid_slope(h)
    d_W1 = X.T @ d_h
    d_b1 = d_h.sum(axis=0, keepdims=True)

    W2 -= lr * d_W2
    b2 -= lr * d_b2
    W1 -= lr * d_W1
    b1 -= lr * d_b1

    if epoch % 2000 == 0:
        print(f"epoch {epoch:5d}  loss {loss:.5f}")

print("\nfinal predictions")
h = sigmoid(X @ W1 + b1)
out = sigmoid(h @ W2 + b2)
for inp, o in zip(X, out):
    print(inp, "->", round(float(o[0]), 3), "=>", int(o[0] > 0.5))