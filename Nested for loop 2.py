#print a right angled triangle
row = int(input('How many rows? : '))
symbol = input('Symbol?: ')
for i in range(row):
    for j in range(i + 1):
        print(symbol, end=' ')
    print()
#the outer loop iterates from 0 to i - 1 until i == input value
#It genertes a sequence of numbers upto but not including the specified number

#print a right angles triangle upside down
for i in range(row, 0, -1):
    for j in range(i):
        print(symbol,end='')
    print()
#the inner loop generates a sequence of numbers from 0 upto i - 1
#this mens that this loop iterates i number of times
#the outer loop generates a sequence of numbers starting from i and ending at 1. it decreases by 1

