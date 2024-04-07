# write a program that determines the largest number from a list of numbers
# take input from user
# you cannot use inbuilt function max
# you can use split and range function
user_prompt = input('Enter your numbers : ')
number_list = user_prompt.split(' ')
length = len(number_list)
for item in range(length):
    number_list[item] = int(number_list[item])
# print(number_list)
# initially set the largest number as the first and compare all the rest to it
max_number = number_list[0]
for item in number_list:
    if item > max_number:
        max_number = item
else:
    print(f'The maximum number is {max_number}')

