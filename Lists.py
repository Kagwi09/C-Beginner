# a variable can store multiple values of different types
list1 = ['Sidney', 'Mwangi', 28, 1.65, 45]
list2 = [2, 10, -50, 13, 19, -9]
print(list1)
print(list1[0])
print(list1[-1])
print(list1[1:-2])
# sort function sorts the values in ascending order
list2.sort()
print(list2)
print(min(list2))
# use append function to add another value to the end of the list. One value at a time
list2.append(45)
print(list2)
# use insert function to add a value at a specific index
list2.insert(2, 30)
print(list2)
# use extend function to add multiple values at the end of the list
list2.extend([53, 47, 59])
print(list2)
# replace the values at the indices indicated
list2[1:4] = (0, 2, 5)
print(list2)
# use remove function to remove the first instance of a value
list2.remove(0)
print(list2)
# use pop function to remove a value from a list
# without any argument, it removes the last value
print(list2.pop())
print(list2)
print(list2.pop(2))
print(list2)
# you can find more list methods online

# NESTED LISTS
# it's a list within a list
list3 = [[23, 29], [17, 'Me'],  [45, 67]]
print(len(list3))
# the inner list is considered as one item in the list
print(list3[2])
print(list3[0][1])
print(f'{list3[0]}\n{list3[1]}\n{list3[2]}')

