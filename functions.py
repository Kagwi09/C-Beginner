# it's a block of code that performs a specific task when called
# function has to be defined before it is called.
# skip 2 blank lines before calling
# function can be called several times
# you can add parameters in () and a return value.
# the function definition and body are mandatory
# there are two types of functions; built in and user defined
# built-in functions are already defined e.g. print
def greet():
    print('Hi', end=' ')
    print('Sid')


greet()
greet()


# FUNCTIONS WITH ARGUMENTS
def greet(name):
    print(f'Hi {name}')
    print('How are you ?')


greet('Sid')
greet('Mwangi')

# name is a parameter that stores the value of the argument passed when the function is called
# Parameter -  a variable name used to store the value of an argument
# Argument - it's a value that is stored in a parameter when the function is called
# the number of arguments passed should be equal to the parameters

# TYPES OF ARGUMENTS
# 1. POSITIONAL ARGUMENTS
# The order of parameters matches with the order of arguments


def greet(name,  gender):
    print(f'Hi {name}')
    print(f'You are {gender}')


greet('Sid', 'Male')

# 2. KEYWORD ARGUMENTS
# it's done by associating a parameter with its subsequent argument using (=)
# By assigning them, you don't have to list the arguments in the same order as parameters


def greet(name, gender):
    print(f'Hi {name}')
    print(f'You are {gender}')


greet(name='Sid', gender='Male')

# 3. DEFAULT ARGUMENTS
# The argument is defined in the parameters.
# if you don't provide an argument during calling, it picks the default argument
# if a value is provided as an argument during calling, it automatically overrides the default value
# the default argument should be provided after non default arguments.


def greet(name, age, gender='Male'):
    print(f'Hi {name}')
    print(f'You are {gender}')
    print(f'You are {age} years old')


greet(name='Sid', age=28)

# 4. ARBITRARY ARGUMENTS
# are of 2 types. Positional and Keyword
# a) Arbitrary positional arguments
# they are indicated using one (*args)
# the arguments are accessed in the form of a tuple


def add(*num):
    c = 0
    for i in num:
        c += i
    print(f'The sum is {c}')


e = int(input('Enter the first number : '))
f = int(input('Enter the second number : '))
g = int(input('Enter the third number : '))
add(e, f, g)

# b) Arbitrary Keyword argument
# are indicated using two ** (**kwargs)
# the arguments are accessed in the form of a dictionary.
# a dictionary has a key and a value
# e.g name = 'Sid'. name is the key and Sid is the value
# if you want to pass *args and ** kwargs. The * arg should always come first


def info_person(**details):
    for key, value in details.items():
        print(key, value)


info_person(name='Sid', age=30, gender='male')
info_person(name='Charles', age=28, gender='male')