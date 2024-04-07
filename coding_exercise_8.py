# ditto coding ex 7 but you can use len function
user_prompt = input('What is your height in cm ? : ')
height = user_prompt.split(' ')
for item in height:
    length = len(height)
for item in range(length):
    height[item] = float(height[item])
total = 0
for item in height:
    total += item
    avg = round(total / length)
print(f'The average height is {avg}')
