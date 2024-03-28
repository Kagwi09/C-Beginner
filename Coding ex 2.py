#Write a program that calculates the BMI of a person in int form.
#this program should also tell you which category of BMI you fall in
# BMI = WEIGHT/HEIGHT ^ 2
weight = float(input('What is your weight? (kg) : '))
height = float(input('What is your height? (m) : '))
BMI = weight // (height**2)
print('Your BMI is : ' + str(BMI))
if BMI <= 18.4:
    str1 = 'You are underweight and'
    if BMI < 16.0:
        print(f'{str1} severely thin')
    elif 16.0 <= BMI <= 16.9:
        print(f'{str1} moderately thin')
    else:
        print(f'{str1} mildly thin')
elif 18.5 <= BMI <= 24.9:
    print('You are in the normal range')
elif 25.0 <= BMI <= 29.9:
    print('You are overweight and pre-obese')
else:
    str2 = 'You are obese '
    if 30.0 <= BMI <= 34.9:
        print(f'{str2} (class 1)')
    elif 35.0 <= BMI <= 39.9:
        print(f'{str2} (class 2)')
    else:
        print(f'{str2} (class 3)')
print('Thank you!')


#Write a program that determines how many days, weeks and months we have left if I live up to 90 years old
age = int(input('How old are you? : '))
old_age = int(input('What age do you expect to live to?: '))
months = (old_age - age) * 12
weeks = (old_age - age) * 52
days = (old_age - age) * 365
print(f'You have {months} months, {weeks} weeks and {days} days left')