# Task 8 - Area of triangle using Heron's formula

a = 5
b = 6
c = 7

# uncomment these to take input from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

semi_perimeter = (a + b + c) / 2

area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)