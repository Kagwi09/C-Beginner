# can contain a dictionary within a dictionary or a list within a dictionary
# basic syntax is dict = {key {dict1}, key{dict2}, key [list]}
# the nesting can go on in multiple levels
student_data = {
    'Jenny': {'roll_no': 92, 'age': 20, 'course': 'Python'},
    'Harry': {'roll_no': 78, 'age': 20, 'course': 'Python'},
    'Dimpy': {'roll_no': 56, 'age': 20, 'course': 'Python'},
    'Rahul': {'roll_no': 76, 'age': 20, 'course': 'Python'},
    'Aniket': {'roll_no': 99, 'age': 20, 'course': 'Python'},
    'Prem': {'roll_no': 34, 'age': 20, 'course': 'Python'}
}
print(student_data)
print(student_data['Jenny'])

# access an individual key value in the nested dict
print(student_data['Jenny']['age'])

# add a new nested element in the dict
student_data['Jenny']['Phone_no'] = 457465
print(student_data['Jenny'])

# delete a nested dict
del student_data['Jenny']['Phone_no']
print(student_data['Jenny'])

# nested list within a dict
travel_location = {
    'Nairobi': ['Giraffe center', 'KICC', 'National park'],
    'Mbs': ['Old city', 'Fort Jesus', 'Nyali'],
}
print(travel_location)
print(travel_location['Nairobi'])

# nested dict within a list
student_data1 = [
    {
     'Name': 'Jenny',
     'roll_no': 92,
     'age': 20,
     'course': 'Python',
     'Phone_no': 978786
    },
    {
        'Name': 'Harry',
        'roll_no': 78,
        'age': 20,
        'course': 'Python'
    },
]
print(student_data1)
print(student_data1[0])
print(student_data1[0]['Phone_no'])