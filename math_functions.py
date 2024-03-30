import math
pi = -3.5486
print(round(pi))
#rounds up to the nearest integer. Anything over .5 is rounded to the next int
print(round(pi, 2))
#rounds up to two decimal places

print(round(11.5))
print(round(12.5))
#when the float value is .5, the program rounds to the nearest even integer

print(round(674, -1))
print(round(678, -1))
print(round(675, -1))
print(round(674, -2))
print(round(678, -3))
print(round(675, -4))
#when you round a number to a negative, it rounds it to the closest multiple of ten, hundred or thousand depending on the -ve value
#tie breaking rule(rounding to the nearest even integer) applies

print(math.ceil(pi))
#rounds up to the largest int

print(math.floor(pi))
#rounds down to the lowest int

print(math.fabs(pi))
#prints the absolute value. How far away its is from 0

print(math.pow(pi, 2))
#prints the power of a variable.
#you can also use a **

print(math.sqrt(400))
#prints the square root of an integer.

x, y, z = 1, 2, 3
print(max(x, y, z))
#prints the largest value from a list of variables
print(min(x, y, z))
#prints the smallest value from a list of variables
