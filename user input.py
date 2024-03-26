#input("What is your name? : ")
#the answer is displayed in the terminal.
#you can assign a variable to the the input
name: str = input("what is your name? : ")
print('Hello '+ name)
#The input is always a string data type. To use an int or float, you have tp typecast
age = int(input('How old are you ? :'))
#the age variable is typecast as an int so that the input can be an integer.
print('I am ' + str(age) + ' ' + 'years old.')
height = float(input('What is your height ? :'))
print('I am ' + str(height) +' ' + 'cm')
#the int and float variables have to be typecast back to strings in the print function