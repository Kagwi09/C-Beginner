import statistics
# a return statement is a special statement used INSIDE  a function
# the program views the return statement as the end of execution
# any statement after the return statement is ignored


def add(a, b):
    c = a + b
    return c


print(add(5, 4))

# write a program that formats a name into proper case


def proper_case(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f'{formatted_f_name} {formatted_l_name}'


print(proper_case('sid', 'MWANGI'))

# RETURN STATEMENT WITH MULTIPLE VALUES


def mean_median_mode(list1):
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)


mn, me, md = mean_median_mode([3, 5, 45, 3, 2, 1, 89])
print(f'{mn}, {me}, {md}')


def add(d, e):
    f = d + e
    if d == 0 and e == 0:
        return
    else:
        return f


first_no = int(input('Enter the first number. : '))
sec_no = int(input('Enter the second number. : '))
total = add(first_no, sec_no)
print(f'The total is {total}')


def add1(final):
    return final + 1


final_output = add1(total)
print(f'The final total is {final_output}')


# PRINT VS RETURN
# The benefit of using return over print() is that the return value
# e.g. total (above) can be used as a variable in another function
# This is not the case with print()