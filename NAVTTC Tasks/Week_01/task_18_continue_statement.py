# Task 18 - continue

for n in range(1, 11):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

for ch in "programming":
    if ch == "m":
        continue
    print(ch, end="")
print()

nums = [4, -2, 7, -9, 10]
total = 0
for n in nums:
    if n < 0:
        continue
    total += n
print("sum of positives:", total)

# continue in while
i = 0
while i < 8:
    i += 1
    if i == 3 or i == 6:
        continue
    print("i is", i)

lines = ["hello", "", "world", "", "python"]
for line in lines:
    if line == "":
        continue
    print(line)
