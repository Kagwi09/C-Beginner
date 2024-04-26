# write a program that determines the days in a certain month of a certain year
def no_of_days(mnth, yr):
    if mnth == '1' or mnth == '3' or mnth == '5' or mnth == '7' or mnth == '8' or mnth == '10' or mnth == '12':
        days = '31'
        return f'The number of days is {days} '
    elif mnth == '4' or mnth == '6' or mnth == '9' or mnth == '11':
        days = '30'
        return f'The number of days is {days}'
    elif mnth == '2':
        if yr % 100 == 0:
            if yr % 400 == 0:
                days = '29'
                return f'The number of days is {days}'
            else:
                days = '28'
                return f'The number of days is {days}'
        else:
            if yr % 4 == 0:
                days = '29'
                return f'The number of days is {days}'
            else:
                days = '28'
                return f'The number of days is {days}'


month = input('Enter the month : ')
year = int(input('Enter the year : '))
print(no_of_days(month, year))
