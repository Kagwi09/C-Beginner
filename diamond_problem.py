class A:

    @staticmethod
    def display():
        print('display from A class')


class B(A):
    def display(self):
        print('display from B class')


class C(A):
    @staticmethod
    def show():
        print('Hi from C class')

    def display(self):
        print('display from C class')


class D(B, C):
    pass

    def display(self):
        print('print from D class')


d1 = D()
d1.display()
# MRO looks for a function from left to right before going deeper.
# in the case of display function, the order is
# D -> B -> C -> A
# print(D.mro())
# In much more complex cases, an algorithm called c3 linearization is used