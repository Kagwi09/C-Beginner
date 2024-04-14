# write a program that determines if a number is prime or not
def prime_num(digit):
    is_prime = True
    if digit == 1:
        is_prime = False
        print("It's not a prime number.")
    for i in range(2, digit):
        if digit % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


num = int(input('Enter your number : '))
prime_num(num)