#ARITHMETIC OPERATORS
#(+) add, (-) subtract), (*) multiply, (//) int division, (/) float division (%) modulus / remainder
#use ** to get the power
print(4**2)
print(4/2)
print(4//2)
#BODMAS rules apply
#in an arithmetic problem where multiple operators are in the same equation, the program
#prioritizes BODMAS rules meaning operations happen from left to right
#the only exception is with the power operator
print(5+2*3-1+10/5)
# multiplication -> division ->addition -> subtraction

#ASSIGNMENT OPERATORS
#shorthand assignment operators : +=, -=, *=, /=, %=, **=
a, b =4, 3
c = a + b
a += 2
c += a
print(c)
#multiple assignments allows one to assign multiple variables in one line of code
full_name, age, height, adult = 'Charles Mwangi', 28, 165.5, True
print(full_name)
print(age)
print(adult)
print(height)
#Can also be used to assign multiple variables with the same value
Sidney = Charles = Kagwi = Mwangi = 28
print(Sidney)
print(Charles)
print(Kagwi)


#LOGICAL OPERATORS
#the not opertor should be used with brackets
#not basically turn a statement false
age = int(input('how old are you? :'))
if age >= 18 and age < 100:
    print('You are an adult')
elif age >= 100:
    print('You are a centenarian')
elif age < 18 and age >= 0:
    print('You are a child')
if not (age >= 0):
    print('error')

#BITWISE OPERATORS
#Work on bits( binary numbers)
#they are (&) bitwise and, (|) bitwise or, (^) XOR, (~) complement (not), (<<) left shift, (>>) right shift
x, y = 5, 4
# 5 in binary is 0101 and 4 is 0100
print(x & y)
#bitwise and means same. if two numbers are the same then it will give you that number.
# if they are different you get 0

print(x | y)
#bitwise or. if two numbers are zero, it gives zero, if its one then it will give you 1.
# if they are different you get 1

print(x ^ y)
#bitwise xor means that if the bits are the same, it'll give 0.
# if they are different you get 1

#bitwise complement
#basically, a negation of any number ~x = -(x+1)
print(~x)
print(~y)

#bitwise leftshift. It shifts the bits to the left and adds 0's at the end
# 5 =0101
#5 << 2 = 010100 = 20
#in 8 and higher bit, you can discard the 0's at the start and replace them
#with 0's at the end. This cannot be done in this 4 bit case since there's a 1
#you always ain bit with left shift
#basically a left shift of any number (x << y) = X x (2 pow y)
print(x  << 4)
print(y << 2)

#bitwise right shift
#always loses bits
#5 = 0101
#5 >> 2 = 0001
#basically a right shift of any number (x >> y) = x/ (2 pow y) in int format not float
print(x >> 2)
print(y >> 2)
