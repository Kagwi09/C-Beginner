#Write a program that determines the final price for a pizza order
#small pizza = $ 10, medium pizza = $ 15, large pizza is $ 22
#pepperoni for medium pizza = $ 3, for medium and large its $ 5
#extra cheese for any size is $ 2

order = input('Size of pizza ? (S,M,L) : ')
bill = 0
str1 = 'Your bill is $'
str2 = 'Your new bill is $'
if order == 'S' or order == 's':
    bill = 10
    print(f'{str1} 10')
    pep = input('Do you want pepperoni? (Y/N) : ')
    if pep == 'Y' or pep == 'y':
        bill = 13
        print(f'{str2} 13')
    else:
        bill = 10
        print(f'{str1} 10')
elif order == 'M' or order == 'm':
    bill = 15
    print(f'{str1} 15')
    pep = input('Do you want pepperoni? (Y/N) : ')
    if pep == 'Y' or pep == 'y':
        bill = 20
        print(f'{str2} 20')
    else:
        bill = 15
        print(f'{str1} 15')
else:
    bill = 22
    print(f'{str1} 22')
    pep = input('Do you want pepperoni? (Y/N) : ')
    if pep == 'Y' or pep == 'y':
        bill = 27
        print(f'{str2} 27')
    else:
        bill = 22
        print(f'{str1} 22')
extra_cheese = input('Do you want extra cheese? (Y/N) : ')
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill = bill + 2
    print(f'Your total bill is $ {bill}')
else:
    print(f'Your total bill is $ {bill}')
print('Thank you!')
