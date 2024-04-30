# scope refers to the area where you can use variables, function or classes
# local scope allows a variable, function or class to be used within a specific program. It cannot be executed outside
# this program
# a variable created outside  a function is in global scope

a = 10


def display():
    #a  = 15
    print(a)


display()

# the first declaration of a makes it a global variable
# this means that it can be used in multiple programs
# however in the event that a similar variable is declared as both local and global,  the program prioritizes
# the local variable


def add1(num):
    c = num + a
    print(c)


add1(4)

# c in the above example is a local variable
# you cannot modify a global variable e.g (a += 1) when a = 10 unless you use the global keyword


def add():
    global a
    a += 1
    print(a)


add()

# you can also use the global keyword to create a global variable inside a function


def add():
    global b
    b = 5
    print(b)


add()