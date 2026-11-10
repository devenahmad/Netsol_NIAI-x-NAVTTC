# Task 6 - Sq Root of complex number

# cmath works for negative and complex numbers, normal math would crash
import cmath

num = 1 + 2j

# to take the number from the user
# num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

print('sqrt of -4 is', cmath.sqrt(-4))