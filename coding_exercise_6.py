# Write a program that prompts a user to input a location where
# they want to hide some data e.g a password in a 3 x 3 matrix
# this location should be ,marked with an 'x'
list1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(f'{list1[0]}\n{list1[1]}\n{list1[2]}')
position = input('Where do you want to place your data? (RC) : ')
row_position = int(position[0])
column_position = int(position[1])
row_number = list1[row_position - 1]
row_number[column_position - 1] = 'x'
print(f'{list1[0]}\n{list1[1]}\n{list1[2]}')
