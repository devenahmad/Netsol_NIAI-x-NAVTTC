# Task 27 - user defined exceptions

class NegativeAmountError(Exception):
    def __init__(self, amount, message="Amount cannot be negative"):
        self.amount = amount
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.amount}"


def check_amount(amount):
    if amount < 0:
        raise NegativeAmountError(amount)
    return amount


try:
    amount = float(input("Enter amount: "))
    check_amount(amount)
    print("Valid amount:", amount)
except NegativeAmountError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid number")


class NotEnoughMoneyError(Exception):
    def __init__(self, balance, wanted):
        self.balance = balance
        self.wanted = wanted
        super().__init__(f"balance is {balance} but you asked for {wanted}")


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError(amount, "can't deposit a negative amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError(amount, "can't withdraw a negative amount")
        if amount > self.balance:
            raise NotEnoughMoneyError(self.balance, amount)
        self.balance -= amount


acc = Account(500)

try:
    acc.deposit(200)
    print("balance:", acc.balance)
    acc.withdraw(1000)
except NotEnoughMoneyError as e:
    print("failed:", e)
    print("short by", e.wanted - e.balance)

try:
    acc.deposit(-50)
except NegativeAmountError as e:
    print("failed:", e)


# a simple age check
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You entered: {self.age}"


def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return age


try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Valid age:", age)
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a whole number")


def check_adult(age):
    if age < 18:
        raise InvalidAgeError(age, "must be 18 or older")
    print("age ok")


for a in (25, 12):
    try:
        check_adult(a)
    except InvalidAgeError as e:
        print("age", a, "->", e)