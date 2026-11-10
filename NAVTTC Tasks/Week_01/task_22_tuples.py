# Task 22 - tuples

t = (1, 2, 3, 4, 5)
print(t)
print(t[0], t[-1], t[1:3])

# single item tuple needs a comma
one = (7,)
print(type(one), type((7)))

# can't change - error handling
try:
    t[0] = 100
except TypeError as e:
    print("error:", e)

nums = (1, 2, 2, 3, 2, 4)
print("count of 2:", nums.count(2))
print("index of 3:", nums.index(3))

# unpacking
a, b, c = (10, 20, 30)
print(a, b, c)

first, *rest = (1, 2, 3, 4)
print(first, rest)

x, y = 5, 9
x, y = y, x
print(x, y)

print((1, 2) + (3, 4))
print((0,) * 4)

# tuple to list and back to change something
l = list(t)
l[0] = 100
t = tuple(l)
print(t)

# returning a tuple from a function
def stats(items):
    return min(items), max(items), sum(items) / len(items)

print(stats([3, 8, 1, 6]))

# tuples as dictionary keys (lists can't do this)
points = {(0, 0): "origin", (1, 2): "point a"}
print(points[(1, 2)])