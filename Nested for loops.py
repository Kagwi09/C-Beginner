#the inner loop finishes all of its iterations before finishing one iteration of the outer loop
row = int(input('How many rows? :  '))
column = int(input('How many columns? :  '))
symbol = input('Symbol : ')
for i in range(row):
    for j in range(column):
        print(symbol)
    print()
#This code will print in # . All in a new line.(default)
#it executes all columns (each in a new line) then executes the first row and so forth
# The second print statement tells the code to jump a line after executing
#Basically it executes all columns and row 1, a new line and so forth.
for i in range(row):
    for j in range(column):
        print(symbol, end=' ')
    print()
#This code does the same thing except the end = function gives it new instructions
#By default, print function ends with a new line
#end function adds any string to the end of output
#by passing a whitespace to the end parameter(end=''), you instruct the code to identify
#the end character by the whitespace and not a new line
#the second print statement tells the code to jump to a new line.
for i in range(row):
    for j in range(column):
        print(symbol, end=' ')
    print()