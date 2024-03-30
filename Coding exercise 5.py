# write a program that flips a virtual coin and generates a heads or tails feedback
import random

prompt = input('Heads or Tails (H/T) ? : ')
x = random.randint(0, 1)
if x == 0:
    print('Heads')
else:
    print('Tails')

# Write a program that picks the random name of a person from a group of five people
# Don't use the random.choice function
# use the split operator. It splits a string at the point it encounters the specified character
# In this case it's the space (' ')
name = input("Input everyone's first name separated by a space : ")
text = name.split(' ')
length = len(text)
x = random.randint(0, length - 1)
# the length in this case will be five but the list has values from index 0 to 4
print(f'The person paying for dinner is {text[x]}')
