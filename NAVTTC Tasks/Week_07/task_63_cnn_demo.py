# Task 63 - convolutional neural network demo
# part 1: what a convolution actually does (numpy only)
import numpy as np


def convolve2d(img, kernel):
    kh, kw = kernel.shape
    h, w = img.shape
    out = np.zeros((h - kh + 1, w - kw + 1))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = np.sum(img[i:i + kh, j:j + kw] * kernel)
    return out


def max_pool(img, size=2):
    h, w = img.shape
    h2, w2 = h // size, w // size
    out = np.zeros((h2, w2))
    for i in range(h2):
        for j in range(w2):
            out[i, j] = img[i * size:(i + 1) * size, j * size:(j + 1) * size].max()
    return out


img = np.zeros((8, 8))
img[:, 4:] = 1
print("image")
print(img)

edge = np.array([[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]])

conv = convolve2d(img, edge)
print("\nafter edge filter (big numbers = edge found)")
print(conv)

relu = np.maximum(0, conv)
print("\nafter relu")
print(relu)

pooled = max_pool(relu)
print("\nafter max pooling")
print(pooled)

# part 2: a small keras cnn (runs only if tensorflow is installed)
try:
    import tensorflow as tf
    from keras import layers, models
except ImportError:
    print("\ntensorflow not installed, skipping the keras part (pip install tensorflow)")
    raise SystemExit

print("\nbuilding a small cnn for 28x28 grey images")
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(8, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(16, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(32, activation="relu"),
    layers.Dense(10, activation="softmax"),
])
model.summary()

# quick fake data just to show training runs (swap with real mnist: tf.keras.datasets.mnist)
x = np.random.rand(200, 28, 28, 1).astype("float32")
y = np.random.randint(0, 10, 200)
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x, y, epochs=2, batch_size=32, verbose=2)