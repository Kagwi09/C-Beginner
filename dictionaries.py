# information is stored in pairs. A key and a value. Variable 'value' stores information regarding the key
# the basic syntax is dict_name ={key : value}
phone_no1 = {
    'Friend1': 1234,
    'Friend2': 23456,
    'Friend3': 45567
}
print(phone_no1)

# you can also make a dictionary using dict function
phone_no2 = dict({
    'Friend4': 1234,
    'Friend5': 23456,
    'Friend6': 45567
})
print(phone_no2)
print(phone_no2['Friend4'])

# in python 3.7 and above, dictionary items are ordered. That order can't be changed
# eys are immutable (unchangeable) but values are mutable
# duplicate keys are not allowed. If there are duplicate values, only the last key is considered

# if you want to change the value of a key you can pass it as follows
phone_no2['Friend4'] = 9865
print(phone_no2)

# values can be of any data type since they are mutable
# keys can only be numbers(int), tuples or strings which are immutable

# dictionaries can also be nested
phone_no2['Friend7'] = {7896, 89752, 99089}
print(phone_no2)
phone_no2['Friend5'] = {'work': 4567, 'home': 5364}
print(phone_no2)
print(phone_no2['Friend5'])
print(phone_no2['Friend5']['work'])

# you can use the get function to access the value of a key
# you need to be case-sensitive
print(phone_no2.get('Friend6'))

# you can use del function to remove an item in a dictionary
del phone_no2['Friend4']
print(phone_no2)
# you can also pop function to remove an item
phone_no2.pop('Friend6')
print(phone_no2)
# you can use the popitem function to remove the last key and value in a dictionary

# you can print keys and values independently
print(phone_no1.keys())
print(phone_no1.values())
# the item function displays all the items in a dictionary in the form of tuples
print(phone_no1.items())

# you can also use a for loop to access item in a dictionary
for i in phone_no1:
    print(i, phone_no1[i])
# i prints the key, phone_no[i] prints the values

# you can also use the item function
for i in phone_no1.items():
    print(i)
# the items function prints both key and value
print(phone_no1)
phone_no1.update({'Friend4': 8907})
print(phone_no1)
