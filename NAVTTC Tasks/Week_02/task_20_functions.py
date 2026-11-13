# Task 20 - User defined functions

def greet(name):
    print("hello", name)


def add(a, b):
    return a + b


def power(base, exp=2):
    return base ** exp


def total(*nums):
    s = 0
    for n in nums:
        s += n
    return s


def info(name, age, city="lahore"):
    print(name, age, city)


def min_max(items):
    return min(items), max(items)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# variable scope
x = 10 # global
print("global:", x)


def show_scope():
    x = 5          # local x
    print("local - inside function:", x)


greet("ali")
print(add(3, 4))
print(power(5), power(2, 10))
print(total(1, 2, 3, 4, 5))
info("sara", 22)
info(age=19, name="bilal", city="karachi")
lo, hi = min_max([4, 9, 1, 7])
print("min", lo, "max", hi)
print([n for n in range(1, 30) if is_prime(n)])
print("5! =", factorial(5))
show_scope()
print("outside:", x)

# lambda, map, filter (pre-made)
sq = lambda n: n * n
print(sq(6))
print(list(map(lambda n: n * 2, [1, 2, 3])))
print(list(filter(lambda n: n % 2 == 0, range(10))))


# nested function
def outer():
    def inner():
        return "i am inside"
    return inner()


print(outer())