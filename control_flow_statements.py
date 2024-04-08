# There are 3 loop control statements. Break, continue and pass

# BREAK
# Can only be used in FOR and WHILE loop
# It is used to exit from a loop. Any statement within that condition (if) after the break statement
# will not be executed
# Any statement outside the block of code will be executed with an exception to else statements
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        break
    print('control')
print('flow')
# in this while loop, 7 is not printed
# as the program iterates and gets to 6, count += 1 becomes 7
# 'The program breaks from the iteration

list1 = ['Hi', 'Hello', 'Hey']
names = ['Sidney', 'Charles', 'Mwangi']

for item in list1:
    for name in names:
        print(f'{item} {name}')
        if item == 'Hey' and name == 'Charles':
            break
    print('Out of inner loop')
print('Out of outer loop')
# In this for loop, the if condition is satisfied before the loop is broken

# CONTINUE
# It's the opposite of break. It instructs the program to continue with the iteration
# Any statement within that condition (if) after the continue statement will not be executed
# It basically skips that statement
# the program loops back to the outer conditional statement.
# Once the program loops back, the next iteration is executed
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        continue
    print('control')
print('flow')
# in this while loop, 7 is printed, but 'control' is not printed after 6
# as the program iterates and gets to 6, count += 1 becomes 7
# 'control' is skipped and 7 is printed out
list1 = ['Hi', 'Hello', 'Hey']
names = ['Sidney', 'Charles', 'Mwangi']

for item in list1:
    for name in names:
        print(f'{item} {name}')
        if item == 'Hey' and name == 'Charles':
            continue
        print('How are you?')
    print('Out of inner loop')
print('Out of outer loop')
# in this for loop, the program prints 'Hey Charles' and loops back and prints 'Hey Mwangi'
# The statement in the if condition is skipped and the program loops back

# PASS
# Tells the program to do nothing
# Defines an empty function / loop
# Basically acts as a placeholder in a loop or function that can be edited in future to some meaningful code
