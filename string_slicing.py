#Can be done using indexing [] or using the slice function slice()
#CAN ONLY BE DONE TO STRING VARIABLES
#INDEXING
full_name = 'Sidney Charles Kagwi Mwangi'
print(len(full_name))
print(full_name.find('y'))
first_name = full_name[0:6]
#or type first_name = full_name[:6]
print(first_name)
print(full_name.find('M'))
last_name = full_name[21:27]
# or  type last_name =full_name[21:]
print(last_name)
alias = full_name[0:27:1]
# or type alias = full_name[::1]
print(alias)
alias = full_name[0:27:2]
# or type alias = full_name[::2] to skip every alternate letter.
print(alias)
reversed_name = full_name[::-1]
print(reversed_name)
#reverses name
#SLICE FUNCTION
website1 = 'www.google.com'
slice1 = slice(4,10)
#or type slice1 = slice(4,-4)
print(website1[slice1])
