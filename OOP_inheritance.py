# it enables a newly created (child/ derived / sub) class to inherit attributes and methods
# from a parent/ base/ super class
# basic syntax ; class Derived ClassName(Base ClassName):
# the child class can have its own attributes and methods
#  child class can have call a function in the parent class and implement it in its own way(overriding)
# you can access a method in the base class while in the child class using the super() function
# if you have used the init function in the parent class, you have to specifically name it in
# the super function (super().__init(self))
# if there's a parameter in the init function, you have to include it
# TYPES OF INHERITANCE

# 1. Single inheritance
# has only one child class
class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.heart = num_heart

    @staticmethod
    def eat():
        print('I can eat ')

    @staticmethod
    def work():
        print('I can work')


class Male(Human):

    def __init__(self, name, hrt):
        super().__init__(hrt)  # fetches init function
        self.user_name = name

    @staticmethod
    def flirt():
        print('I can flirt')
# method of child class

    def work(self):
        super().work()  # fetched method from parent class
        print('I can code')  # overridden method (work())


male1 = Male('Sid', 1)
# male1.eat()
# male1.flirt()
male1.work()
print(male1.num_eyes)  # fetches attribute from parent class
print(male1.user_name)

# 2. Multiple inheritance
# child class inherits from two or more parent classes
# if you have similar methods on 2 or more parent classes, the fetched method outputs
# in the order they were declared in the child class
# init functions also follow the MRO


class Human:

    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.heart = num_heart

    @staticmethod
    def eat():
        print('I can eat ')

    @staticmethod
    def work():
        print('I can work')


class Male:
    def __init__(self, name):
        self.user_name = name

    @staticmethod
    def flirt():
        print('I can flirt')
# method of child class

    @staticmethod
    def work():
        print('I can code')


class Boy(Human, Male):
    def __init__(self, name, heart, language):
        super().__init__(heart)
        Male.__init__(self, name)  # defines which parent class attribute is derived from
        # the init function must contain the same parameters as the parent class
        self.p_language = language

    @staticmethod
    def sleep():
        print('I can sleep')

    def work(self):
        print('I can test')

    def display(self):
        return f'Hi i am {self.user_name} and I am learning to use {self.p_language}'


boy1 = Boy('Kagwi', 1, 'Python')
print(boy1.num_nose)
print(boy1.user_name)
print(boy1.heart)
print(boy1.p_language)
print(boy1.display())
# boy1.flirt()
# boy1.work()  # outputs the child's method first, then first parent method
# Male.work()  # outputs the Male parent's method
# print(Boy.mro())  # method resolution order

# 3. MULTILEVEL INHERITANCE
# It involves inheritance from a child class.
# inheritance can go as far as one wants to
# function calling follows MRO
# the order goes ascends from the outermost child class to the parent class


class Human:
    def __init__(self, heart):
        self.eyes = 2
        self.num_heart = heart

    @staticmethod
    def eat():
        print('I can eat ')

    @staticmethod
    def work():
        print('I can work')


class Male(Human):
    def __init__(self, heart, name):
        super().__init__(heart)
        self.u_name = name

    @staticmethod
    def sleep():
        print('I can sleep')


class Boy(Male):
    def work(self):
        Human.work()  # or use the super method to access the work function
        print('I can code')


class Programmer(Boy):

    def work(self):
        print('I can write programs')


boy1 = Boy(1, 'sid')
boy1.eat()
boy1.work()
# print(Boy.mro())
# prog1 = Programmer()
# prog1.work()
print(boy1.eyes)

# 4. HIERARCHICAL INHERITANCE
# It involves multiple child classes inheriting from one parent class


class Human:
    def __init__(self, name, age):
        self.u_name = name
        self.u_age = age

    def show_details(self):
        print(f'name : {self.u_name}, age : {self.u_age}')

    @staticmethod
    def eat():
        print('I can work')


class Male(Human):

    def __init__(self, name, age, location):
        super().__init__(name, age)
        self.u_location = location

    @staticmethod
    def sleep():
        print('I can sleep')

    def show_details_m(self):
        Human.show_details(self)


class Female(Human):

    @staticmethod
    def work():
        print('I can code')


female1 = Female('sia', 7)
male1 = Male('doug', 7, 'ke')  # once a new attribute is introduced in Male subclass, the parameter should also be added
# female1.eat()
# male1.eat()
human1 = Human('me', 9)
human1.show_details()
female1.show_details()

# 5. HYBRID INHERITANCE
# It's a combination of two or more types of inheritance
# MRO follows rules of specific inheritance types
# MRO of class D is D -> B -> A -> C


class A:

    @staticmethod
    def display():
        print('display from A class')


class B(A):
    def display(self):
        print('display from B class')


class C:
    @staticmethod
    def show():
        print('Hi from C class')


class D(B, C):
    def display(self):
        print('print from D class')


d1 = D()
d1.display()
print(D.mro())