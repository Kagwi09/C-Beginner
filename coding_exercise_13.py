# write a program that multiplies the values of an arbitrary positional argument and arbitrary k.w arguments
def product(*num):
    e = 1
    for i in num:
        e = e*i
    print(f'The products is {e}')


product(2, 3, -6, 8)
product(2, 5, 8, 9, 6)


def product(**digits):
    e = 1
    for key, value in digits.items():
        e *= value
    print(f'The product is {e}')


product(digit1=2, digit2=3, digit3=-6, digit4=8)
product(digit1=2, digit2=5, digit3=8, digit4=9, digit5=6)