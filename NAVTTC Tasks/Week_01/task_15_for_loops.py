# Task 15 - for loops

fruits = ["apple", "banana", "mango"]
for f in fruits:
    print(f)

print("\ncounting 0 to 4")
for i in range(5):
    print(i)

print("\neven numbers from 2 to 10")
for i in range(2, 11, 2):
    print(i)

print("\nletters in python")
for ch in "python":
    print(ch, end=" ")
print()

ages = {"ali": 20, "sara": 22, "bilal": 19}
print("\nages")
for name, age in ages.items():
    print(name, "is", age)

total = 0
for n in range(1, 101):
    total += n
print("\nsum of 1 to 100 =", total)

print("\ntable of 7")
for n in range(1, 11):
    print("7 x", n, "=", 7 * n)

# for with else
for n in range(3):
    print(n)
else:
    print("loop finished normally")