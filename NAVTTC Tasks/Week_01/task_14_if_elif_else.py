# Task 14 - if / elif / else

i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")

# try other values of i to hit the other branches
for i in (10, 15, 20, 99):
    if i == 10:
        print(i, "-> i is 10")
    elif i == 15:
        print(i, "-> i is 15")
    elif i == 20:
        print(i, "-> i is 20")
    else:
        print(i, "-> i is not present")