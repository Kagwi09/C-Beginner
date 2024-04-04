# stores multiples values in a variable
# unlike lists, its stores the values in brackets
# unlike list, they cannot be changed. You can't add or remove data
# like lists, you can use mixed data types in the same variable
# similar to lists, duplicate values are allowed
# like lists, you can combine two tuples into one or nest them together
# if you only want to store one value in a tuple, place a comma after it
# otherwise python will view it as an int,str, float or bool
tuple1 = (12, 12, 45, 'tree')
tuple2 = (33, -12, 87, 'one')
print(tuple1)
print(tuple1[3])
tuple3 = (tuple1 + tuple2)
print(tuple3)
tuple4 = (tuple1, tuple2)
print(tuple4)
# you can convert a list to a tuple
list1 = [1, 2, 3, 4, 'yeah']
print(tuple(list1))