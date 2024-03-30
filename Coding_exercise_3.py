#Write a program that determines if a year is leap or not
year = int(input('Input your year : '))
str1 ="It's a leap year!"
str2 = "It's not a leap year"
if year % 100 == 0:
    if year % 400 == 0:
        print(str1)
    else:
        print(str2)
else:
    if year % 4 == 0:
        print(str1)
    else:
        print(str2)
