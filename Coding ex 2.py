#Write a program that calculates the BMI of a person in int form.
# BMI = WEIGHT/HEIGHT ^ 2
weight = int(input('What is your weight? (kg) : '))
height = float(input('What is your height? (m) : '))
BMI = int(weight) // int(height**2)
print('Your BMI is : ' + str(BMI))

#Write a program that determines how many days, weeks and months we have left if I live up to 90 years old
age = int(input('How old are you? : '))
old_age = int(input('What age do you expect to live to?: '))
months = (old_age - age) * 12
weeks = (old_age - age) * 52
days = (old_age - age) * 365
print(f'You have {months} months, {weeks} weeks and {days} days left')