# write a program that finds the area and perimeter of a rectangle


class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def perimeter(self):
        p = 2 * (self.l + self.w)
        return p

    def area(self):
        a = self.l * self.w
        return a


rec1 = Rectangle((float(input('Enter the length : '))), (float(input('Enter the width : '))))
print(f'The perimeter is {rec1.perimeter()} m')
print(f'The area is {rec1.area()} m2')
