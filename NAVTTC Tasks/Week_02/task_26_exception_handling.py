# Task 26 - exception handling

try:
    print(10 / 0)
except ZeroDivisionError:
    print("can't divide by zero")

tests = ["12", "abc", "0"]
for t in tests:
    try:
        n = int(t)
        print("100 /", n, "=", 100 / n)
    except ValueError:
        print(repr(t), "is not a number")
    except ZeroDivisionError:
        print("zero not allowed")

try:
    x = int("5")
except ValueError:
    print("bad")
else:
    print("no error, x =", x)
finally:
    print("finally always runs")

try:
    with open("this_file_does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("file is missing")

try:
    [1, 2, 3][10]
except IndexError as e:
    print("index problem:", e)

try:
    {"a": 1}["b"]
except KeyError as e:
    print("missing key:", e)

try:
    int(None)
except Exception as e:
    print("something went wrong:", type(e).__name__)

def set_age(age):
    if age < 0:
        raise ValueError("age can't be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("caught:", e)

with open("demo.txt", "w") as f:
    f.write("line one\nline two\n")

with open("demo.txt") as f:
    for line in f:
        print(line.strip())
