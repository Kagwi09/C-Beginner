# executes as long as the statement is true
# can result in an infinite loop if the user isn't given an option that closes the loop
# can be used in place of a for loop when the number of iterations is determined by the user
name, age = '', ''
while len(name) == 0:
    name = input('What is your name? :  ')
    # it will execute an infinite loop until the input is answered.
    print('Hello '+name)
    while len(age) == 0:
        age = input('How old are you? : ')
        print('You are ' + ' ' + age + ' ' + 'years old')

# while loop can also be used with else. The else bloc of statement
# is executed when the while loop becomes false
# the else block will not execute if the while loop is terminated forcefully using break
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print('in else block')

count = 1
while count <= 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print('in else block')

# it's important to add an increment statement (+=) in order to close the while loop and prevent infinite loop
# you can also use a decrement value
# you can use boolean values TRUE or FALSE as a condition

# SENTINEL VALUE
# It's provided to terminate a while loop. It can be -1 if you are using +ve value integers
# any value can be used as long as the user has been told what it is

# write a program that generates the sum of numbers generated from a user prompt
# the program will be exited when the user inputs 0

prompt1 = int(input('Enter the number (0 to exit) : '))
total = 0
while not (prompt1 == 0):
    total += prompt1
    prompt1 = int(input('Enter the number (0 to exit) : '))
print(f'The total is {total}')

