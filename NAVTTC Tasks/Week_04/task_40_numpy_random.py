# Task 40 - numpy random
import numpy as np

np.random.seed(42)

print(np.random.randint(100))
print(np.random.randint(1, 7, size=10))
print(np.random.rand())
print(np.random.rand(2, 3))
print(np.random.randn(5))
print(np.random.randint(0, 50, size=(2, 4)))

colors = ["red", "green", "blue"]
print(np.random.choice(colors))
print(np.random.choice([1, 2, 3, 4], size=6))
print(np.random.choice(colors, size=10, p=[0.7, 0.2, 0.1]))

a = np.arange(10)
np.random.shuffle(a)
print(a)
print(np.random.permutation(5))

print(np.random.normal(50, 10, 5))
print(np.random.uniform(0, 1, 3))
print(np.random.binomial(10, 0.5, 5))

big = np.random.normal(100, 15, 100000)
print("mean:", big.mean().round(2), "std:", big.std().round(2))