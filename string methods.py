name, age, gender = "sidney mwangi", '28', 'male'
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
