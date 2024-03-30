#write a program that determines how much you can pay depending on your age and height
#Only people over the age of 8 and over 4.5 ft can ride the carousel
#Adults are required to pay $ 10 while minors between 10 & 13 are required to pay $ 5
#Minors between 13 & 17 pay $ 8
#If a customer wants to take a photo, they will be charged an extra $ 2
height = float(input('What is your height? (feet): '))
if height >= 4.5:
    age = int(input('How old are you? : '))
    if age >= 10:
        bill = 0
        str1 = 'Your ticket is $'
        if 10 <= age <= 13:
            bill = 5
            print(f'{str1} 5')
        elif 14 <= age <= 17:
            bill = 8
            print(f'{str1} 8')
        else:
            bill = 10
            print(f'{str1} 10')

        want_photo = input('Would you like to take a photo? (Y/N) : ')
        if want_photo == 'Y' or want_photo == 'y':
            bill = bill + 2
            print(f'Your total bill is {bill}')

    else:
        print('You are too young for this ride')
else:
    print('You are too short for this ride')
print('Thank you!')
