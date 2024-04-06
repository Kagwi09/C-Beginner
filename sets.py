# like lists and tuples, they also store multiple values in a variable
# they're stored in curly brackets {}
# you can define a set using the set function or using curly brackets.
# Using the set function enables you to create an empty set
#  like lists and tuples, you can also store values of different data types
# you cannot store duplicate values. If they exist, only the first instance is printed out
# when printed, they don't necessarily print in the same order they were initially listed unlike in lists and tuples
# unlike lists and tuples, indexing is not allowed because they don't have a defined order
# like in tuples, the values cannot be changed because indexing is not allowed
# however, like lists, you can add or remove parts of the set using set functions
# you can add a tuple to a set. However, you cannot add a list
# this is because the data in a list can be changed
set1 = {1, -12, 'aloe', True, 1.8}
print(set1)
set2 = set()
print(set2)

# SET METHODS
# adding a value to a set one value at a time
set1.add(80)
print(set1)

# remove a value
set1.remove('aloe')
print(set1)
# you can also use the discard function.
# the only difference with remove is that it will return the values in the variable without an error message
# even when the value doesn't exist. If you use the remove function when the value isn't present
# an error message will be displayed

# clear a set
set1.clear()
print(set1)

set1 = {3, 9, 'fix', -23}

# remove a random value from a set
set1.pop()
print(set1)
print(set1.pop())

# completely remove elements from a set and delete it
# use del
# e.g. del set1

# OPERATIONS ON SETS
set3 = {'aloe', 'clove', 'daisy'}
set4 = {'clove', 'smooth', 'thyme'}
set5 = {'mint', 2, 'smooth', 'yellow'}

# Union of two sets. Is a combination of two or more sets. Similar values appear once
print(set3.union(set4, set5))
print(set3 | set4 | set5)
# the union function can also be used to combine a tuple and a set
# it transforms the tuple into a set and then combines it
print(set3.union(('game', 'go')))
# the update operator can also be used to append a set to another.
set4.update(set5)
print(set4)
# you can also pass a list as a command in the update function to combine it into the set just like
# with a tuple in the example above
# you can also update using by using a '=' set4= set5

# Intersection of sets. Checks which value are similar in both sets
print(set3.intersection(set4))
print(set3 & set4)
# like in unions you can pass a tuple or list to check for intersection with a set
set3.intersection_update(set4)
print(set3)

set3 = {'aloe', 'clove', 'daisy'}
set4 = {'clove', 'smooth', 'thyme'}
set5 = {'mint', 2, 'smooth' 'yellow'}

# Difference (set1 - set2) will give whatever elements that are in set1 and not in set2
print(set3.difference(set4))
print(set3 - set4)
# similarly, you can pass a tuple or a list as an argument
set3.difference_update(set4)
print(set3)

set3 = {'aloe', 'clove', 'daisy'}
set4 = {'clove', 'smooth', 'thyme'}

# Symmetric difference will return values that are in either set but not in both
# this operation does not allow for the comparison of more than two sets. It takes exactly one argument
print(set3.symmetric_difference(set4))
print(set3 ^ set4)
# the second operator can be used on multiple sets e.g. set3 ^ set4 ^ set5
set3.symmetric_difference_update(set4)
print(set3)

set3 = {'aloe', 'clove', 'daisy'}
set4 = {'clove', 'smooth', 'thyme'}
# DISJOINTED SETS
# Two sets are said to be disjointed if they have nothing in common i.e. there's no intersection (empty set)
# You can use the isdisjoint function to check. It returns true if there's nothing in common. False if there's
# something in common
# Doesn't have an operator
# You can pass a list or a tuple as an argument
print(set3.isdisjoint(set4))
print(set3.isdisjoint(set5))

# SUBSETS
# checks if a set is a subset of another
# e.g. set1.issubset(set2) checks if set2 has ALL elements of set1
# it can use an operator (<=)
# you can pass a set or a tuple
print(set4.issubset(set5))
print(set4 <= set5)

# SUPERSETS
# it's the reverse of subsets
# e.g. set1.issuperset(set2) checks if set1 has all elements of set2
# it can be used with an operator (>=)
# you can pass a set or a tuple
print(set4.issuperset(set5))
print(set4 >= set5)

