#executes as long as the statement is true
#can result in an infinite loop if the user isn't given an option that closes the loop
name, age = '', ''
while len(name) == 0:
    name = input('What is your name? :  ')
    #it will execute an infinite loop until the input is answered.
    print('Hello '+name)
    while len(age) == 0:
        age = input('How old are you? : ')
        print('You are ' + ' ' + age + ' ' + 'years old')s
