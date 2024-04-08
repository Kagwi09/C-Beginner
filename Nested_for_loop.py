# basically it executes one instance of the outer loop and all instances of the inner loop before looping back
row = int(input('How many rows? :  '))
column = int(input('How many columns? :  '))
symbol = input('Symbol : ')
for i in range(row):
    for j in range(column):
        print(symbol)
    print()
# This code will print in # . All in a new line.(default)
# it executes all columns (each in a new line) then executes the first row and so forth
# The second print statement tells the code to jump a line after executing
# Basically it executes all columns and row 1, a new line and so forth.
for i in range(row):
    for j in range(column):
        print(symbol, end=' ')
    print()
# This code does the same thing except the end = function gives it new instructions
# By default, print function ends with a new line
# end function adds any string to the end of output
# by passing a whitespace to the end parameter(end=''), you instruct the code to identify
# the end character by the whitespace and not a new line
# the second print statement tells the code to jump to a new line.
for i in range(row):
    for j in range(column):
        print(symbol, end=' ')
    print()
# print a right-angled triangle
row = int(input('How many rows? : '))
symbol = input('Symbol?: ')
for i in range(row):
    for j in range(i + 1):
        print(symbol, end=' ')
    print()
# the outer loop iterates from 0 to i - 1 until i == input value
# It generates a sequence of numbers up to but not including the specified number

# print a right angles triangle upside down
for i in range(row, 0, -1):
    for j in range(i):
        print(symbol, end='')
    print()
# the inner loop generates a sequence of numbers from 0 up to i - 1
# this mens that this loop iterates 'i' number of times
# the outer loop generates a sequence of numbers starting from i and ending at 1. it decreases by 1

