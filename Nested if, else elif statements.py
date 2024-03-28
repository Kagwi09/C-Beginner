#write a program that determines how much you can pay depending on your age and height
#Only people over the age of 8 and over 4.5 ft can ride the carousel
#Adults are required to pay $ 10 while minors between 10 & 13 are required to pay $ 5
#Minors between 13 & 17 pay $ 8
height = float(input('What is your height? (feet): '))
if height >= 4.5:
    age = int(input('How old are you? : '))
    if age >= 18:
        print('Please pay $ 10')
    elif 10 <= age <= 13:
        print('Please pay $ 5')
    elif 13 < age < 18:
        print('Please pay $ 8')
    else:
        print("You are too young for this ride")
else:
    print('You are too short for this ride')
print('Thank you!')
