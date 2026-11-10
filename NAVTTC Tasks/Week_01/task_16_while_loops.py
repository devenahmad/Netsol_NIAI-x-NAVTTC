# Task 16 - while loops

count = 1
while count <= 5:
    print("count is", count)
    count += 1

n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
print("liftoff")

num = 4582
total = 0
while num > 0:
    total += num % 10
    num = num // 10
print("sum of digits of 4582 =", total)

num = 12345
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("reversed:", rev)

x = 100
steps = 0
while x >= 1:
    x = x / 2
    steps += 1
print("took", steps, "halvings to go below 1")

# while with else
i = 0
while i < 3:
    print("i =", i)
    i += 1
else:
    print("while finished")