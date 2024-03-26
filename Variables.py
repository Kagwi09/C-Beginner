first_name = 'Charles'
last_name = 'Mwangi'
full_name = first_name + ' ' + last_name
print(first_name)
print('Hello '+first_name)
print(full_name)
print('Hello ' + full_name)
#Strings cannot be used together with integers. However, if an int is used with quotation marks it becomes a string
age = 27
print(age)
age += 1
print(age)
new_age = "21"
print(new_age)
print('Hello, my name is ' + full_name + " " + 'and I am ' + new_age)
#typecasting convert an int into a string
print('Hello, my name is ' + full_name + " " + 'and I am ' + str(age))
#typecasting can also be used to turn a float into a string
height = 165.5
print('Hello, my name is ' + full_name + " "+'and I am ' + str(age) + " " + 'and' + " " + str(height) + " " + 'cm')
#boolean. True and False have to start with block letters
adult = True
print(adult)
print('Are you over 18 ? :' + str(adult))
print(4/2)
print(4//2)