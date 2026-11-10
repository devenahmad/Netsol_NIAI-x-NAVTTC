# Task 21 - lists

nums = [10, 20, 30, 40, 50]
print(nums)
print("first:", nums[0], "last:", nums[-1])
print("slice 1 to 3:", nums[1:4])
print("every second:", nums[::2])
print("reversed:", nums[::-1])

nums.append(60)
nums.insert(0, 5)
nums.extend([70, 80])
print(nums)

nums.remove(5)
last = nums.pop()
print("popped", last)
del nums[0]
print(nums)

print("30 in list?", 30 in nums)
print("index of 40:", nums.index(40))
print("length:", len(nums))

mixed = [5, 3, 9, 1, 7]
mixed.sort()
print(mixed)
mixed.sort(reverse=True)
print(mixed)

print("sum", sum(mixed), "min", min(mixed), "max", max(mixed))

a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print("b changed too:", b)
print("c stayed:", c)

print([1, 2] + [3, 4])
print([0] * 5)

# 2d list
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(grid[1][2])
for row in grid:
    print(row)

print([n * 3 for n in range(5)])