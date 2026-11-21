# Task 64 - cnn on the cifar-10 dataset
# first run downloads the dataset (about 170 MB), so you need internet once.
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    import tensorflow as tf
    from keras import layers, models
except ImportError:
    print("\ntensorflow not installed (pip install tensorflow)")
    raise SystemExit

class_names = ["airplane", "automobile", "bird", "cat", "deer",
               "dog", "frog", "horse", "ship", "truck"]

QUICK = False

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print("train:", x_train.shape, "test:", x_test.shape)

if QUICK:
    x_train, y_train = x_train[:5000], y_train[:5000]
    x_test, y_test = x_test[:1000], y_test[:1000]

x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
y_train = y_train.ravel()
y_test = y_test.ravel()

model = models.Sequential([
    layers.Input(shape=(32, 32, 3)),

    layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    layers.Flatten(),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(10, activation="softmax"),
])
model.summary()

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

history = model.fit(
    x_train, y_train,
    epochs=3 if QUICK else 15,
    batch_size=64,
    validation_split=0.1,
    verbose=2,
)

loss, acc = model.evaluate(x_test, y_test, verbose=0)
print("\ntest accuracy:", round(acc, 3))

pred = model.predict(x_test[:10], verbose=0).argmax(axis=1)
for i in range(10):
    print("real:", class_names[y_test[i]].ljust(11), "predicted:", class_names[pred[i]])

plt.plot(history.history["accuracy"], label="train")
plt.plot(history.history["val_accuracy"], label="validation")
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend()
plt.savefig("task_64_curves.png")
print("curves saved as task_64_curves.png")

model.save("cifar10_cnn.keras")
print("model saved as cifar10_cnn.keras")