# write a program that calculates the area and circumference of a circle
# a child class should find the volume and surface area of a cylinder
import math


class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.r = radius

    def circumference(self):
        c = round((2 * Circle.pi * self.r), 2)
        return c

    def area(self):
        a = round(2 * (Circle.pi * (self.r ** 2)), 2)
        return a


class Cylinder(Circle):
    def __init__(self, height):
        super().__init__(height)
        self.c_height = height

    def area(self):
        super().area()
        v = round(circle1.area() * self.c_height, 2)
        return v

    def circumference(self):
        super().circumference()
        c_s_a = round((self.c_height * circle1.circumference()) + (self.area() * 2), 2)
        return c_s_a


circle1 = Circle(float(input('Enter your radius(m) : ')))
cylinder1 = Cylinder(float(input('Enter the height of the cylinder(m) : ')))
print(f'The circumference of the circle is {circle1.circumference()} m')
print(f'The area of the circle is {circle1.area()} m2')
print(f'The volume of the cylinder is {cylinder1.area()} m3')
print(f'The surface area of the cylinder is {cylinder1.circumference()} m2')

# pi is a class object attribute
# the value is the same for every instance it is used
