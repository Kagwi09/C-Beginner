# write a program that calculates the sum of all even number from 1 to 100 including 1 and 100
number = 0
for i in range(0, 101, 2):
    number += i
print(number)