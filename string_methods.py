name, age, gender, height, new_age = "sidney mwangi", '28', 'male', 1.6, 30
print('My name is '+name + ' ' 'I am ' +age + ' years old and' + ' ' +  str(height) + ' meters tall' )
#or
print('My name is ',name,  ' ' 'I am ' ,age,  ' years old and' + ' ' ,str(height),  ' meters tall' )
#or
print(f'My name is {name}. I am {age} years old and {height} meters tall' )
print(f'My name is {name}. I am {new_age+2} years old and {height+1} meters tall' )
#the f function introduced allows the print function to print everything as 1 string. The variables are stored in {}
print(len(name))
print(name.find('M'))
#white space is counted during find

print(name.capitalize())
#If there are multiple words in a string or a space, only the first letter is capitalized

print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
#if there's a pace between words in a string, isalspha will return false
print(gender.isalpha())
print(age.isdigit())
print(name.count('i'))
#counts the number of instances a character appears in a string

print(name.replace('i', 'u'))
print(name*3)
