import random
#its an inbuilt module that generates random pseudo random number
#cannot be used for security functions like generating a OTP

x = random.randint(1,9)
print(x)
#generates a random number bewteen 1 and 9. ( 1 =< x <= 9)
# 1 and 9 are included

y = random.randrange(1,9)
print(y)
#generates a randown number between 1 and 9. (1 =< y < 9)
#1 is included but 9 is not

z = random.random()
print(z)
#when passed without an arguement. It generates a randon floati between 0.0 and 1.0
# 0.0 =< x < 1.0
#0.0 is included but 1.0 is not

a = random.uniform(2, 8)
print(a)
#ditto but with a specified range

list1 =[10, 91, 30, 63, 87]
b = random.choice(list1)
print(b)
#prints a random item from a list
nu = random.choices(list1,  k=4 )
print(nu)

random.shuffle(list1)
print(list1)
#shuffles the order items appear in a list
#there are numerous random functions to choose from
