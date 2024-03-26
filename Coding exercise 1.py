#1
string_1 = 'First Program'
string_2 = 'Python print function'
print(string_1 + ' -' + ' ' + string_2)
print('It is declared like this :')
print("print('What to print')")
#note the use of double quotes and single quotes interchangeably because the program will consider everything between the first
#two single quotes as a string and the middle part as code

#2 - swap the values of two varaibles
a = int(input('Enter the value of a : '))
b = int(input('Enter the value of b: '))
temp = a
a = b
b = temp
print('a = '+str(a))
print('b = '+str(b))

#3Write a program that adds the digits of a number
digit = input('What is your number?: ')
ones = digit[1]
tens = digit[0]
sum = int(ones) + int(tens)
print (sum)