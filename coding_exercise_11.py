# Fizz buzz job interview question
# Write a program that generates number from 0 to 100
# if the number is divisible by 3, print Fizz
# if the number is divisible by 5, print Buzz
# if its divisible by both 3 and 5, print FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'FizzBuzz, ', end=' ')
    elif i % 5 == 0:
        print(f'Buzz, ', end=' ')
    elif i % 3 == 0 :
        print(f'Fizz, ', end=' ')
    else:
        print(f'{i}, ', end=' ')