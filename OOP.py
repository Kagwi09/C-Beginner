# composed of classes and objects
# every object has information and does a specific task
# the information is modelled through variables (attributes) and the tasks through functions (methods)
# the attributes and methods are 'attached' to the object
# class is a user defined data type. It works as a prototype for an object
# the basic syntax is class ClassName: , The class name should be in pascal case.
# each word in the class name should start with a capital letter
# when assigning an attribute to an object, add a (.) before the attribute name
# use the init function to initialize an object
# every time you create an object in a class, the init function is called
# The 'hello' statement is printed out twice because the init function is called twice. (Two objects)

class Instructor:
    def __init__(self):
        print('Hello')


instructor_1 = Instructor()
instructor_1.name = 'Sid'
instructor_1.address = 985
instructor_2 = Instructor()
instructor_2.name = 'Mwangi'
instructor_2.address = 300
print(instructor_1.name)
print(instructor_1.address)
print(instructor_2.name)
print(instructor_2.address)
# instructor_1 is an object


class Tutor:
    followers = 0

    def __init__(self, name, address):
        self.tutor_name = name
        self.tutor_address = address

    def display(self, age):
        print(f'Hi {self.tutor_name}, I am {age}')

    def new_followers(self, follower_name):
        self.followers += 1


tutor_1 = Tutor('Charles', 500)
tutor_2 = Tutor('Kagwi', 900, )

tutor_1.display('28')
tutor_2.display('30')
tutor_1.new_followers('Me')
print(tutor_1.followers)

# you can set a default value for each object by assigning an attribute without declaring it in the function
# see followers. By default, every object will have 0 followers
# followers is a class object attribute
# you can update the number of followers by declaring a new function
# the tutor name comes after self because it is an attribute that has been described.
# age doesn't need to have self come before it because it is not an attribute

