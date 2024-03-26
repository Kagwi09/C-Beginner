# if, else, else if statements
#they follow the order of if -> elif -> else or if -> else
# use >=, <= and == to equate
#use COLONS after conditions
#the order of statements matter to prevent a situation where a condition can be determined  to be true by two or more statements
age = int( input('How old are you? : '))
if age == 100:
    print('You are a century old')
elif age >= 18:
    print('You are an adult')
else:
    print("You are a minor")
