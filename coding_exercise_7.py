# write a program that calculates the average height from a list of heights
# you cannot use sum and length functions
# replicate their functions with for loop
# input has to come from a user
# the answer should be rounded off to the nearest whole number
# you are allowed to use split and range functions

# height is the name of list of string input
# list count is the number of elements in the
# h is the index of each element
user_prompt = input('Input the heights : ')
height = user_prompt.split(' ')
list_count = 0
for item in height:
    list_count += 1
for h in range(list_count):
    height[h] = float(height[h])
total = 0
for item in height:
    total += item
    avr = round(total / list_count)
print(f'The average height is {avr}')
