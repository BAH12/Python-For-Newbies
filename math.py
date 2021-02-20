                                PYTHON MATH
Python has a built-in maths functions, including an extensive math module, that allows you to perform mathematical tasks on numbers


                        BUILT-IN MATH FUNCTIONS
The min() and max() functions can ve used to find the lowest or highest value in an iterable
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

The abs() function returns the absolute (positive) value of the specified number
x = abs(-7.25)
print(x)

The pow(x, y) function returns the value of x to the power of y
eg
Return the value of 4 to the power of 3 (same as 4 * 4 * 4)
x = pow(4, 3)
print(x)


                            THE MATH MODULE
Python has a built-in module called math, which extends the list of mathematical functions

To use it, you must import the math module
import math

The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # rounds to 2
print(y)    # returns 1

The math.pi constant, returns the value of PI(3.14...)
import math
x = math.pi
print(x)