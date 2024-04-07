# like in if else statements, the for else statements don't have the else statement indented in the if statement
# the else statement is ONLY executed when the for statement is executed SUCCESSFULLY
# the else statement doesn't execute if there's a break keyword or if there's an error
numbers = [10, 23, -34, 89, 87]
for i in numbers:
    print(f'{i},', end=' ')
else:
    print('list executed successfully')


