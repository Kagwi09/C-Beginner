# used when the number of iterations is limited
# it runs through each element in a sequence and executes the command with each
list1 = ['mint', 'clove', 'sage', 'thyme']
for herb in list1:
    print(f'{herb} is a herb')
    if herb == 'clove':
        print('It is good for cooking pilau')
# herb serves as a placeholder for  each element in the list until all iterations are complete

numbers = [2, 3, 5, -2, 10]
# print the squares of list2 in another list
squares = []
for i in numbers:
    sqr = i ** 2
    squares.append(sqr)
print(squares)