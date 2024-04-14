# write a program that determines the number of cans of paint required to paint a wall
# the parameters should be input by a user
def paint_calc(height, width, coverage):
    area = height * width
    cans = round(area / coverage)
    print(f'You need {cans} can(s)')


a = int(input('What is the height of the wall (m)? : '))
b = int(input('What is the width of the wall (m)? : '))
c = int(input('What is the area covered by one can of paint? (sqm): '))
paint_calc(height=a, width=b, coverage=c)
