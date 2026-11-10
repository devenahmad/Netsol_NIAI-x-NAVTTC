# Task 19 - different ways to loop

# enumerate gives index and value
colors = ["red", "green", "blue"]
for i, c in enumerate(colors):
    print(i, c)

for i, c in enumerate(colors, start=1):
    print(i, c)

# zip loops two lists together
names = ["ali", "sara", "bilal"]
marks = [80, 92, 75]
for n, m in zip(names, marks):
    print(n, "got", m)

for c in reversed(colors):
    print(c)

# (doesn't change the original)
nums = [5, 2, 9, 1]
for n in sorted(nums):
    print(n, end=" ")
print()

d = {"a": 1, "b": 2, "c": 3}
for k, v in d.items():
    print(k, "->", v)

squares = [x * x for x in range(1, 8)]
print(squares)

even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)

for i in range(1, 5):
    print("*" * i)

# iterator by hand
it = iter([10, 20, 30])
print(next(it))
print(next(it))
print(next(it))