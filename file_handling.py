# f1 = open('file_1', 'x')
# x creates a file called file_1.
# use 'x' if you are sure that the file doesn't exist, if f1 is run and file_1 exists, it will return an error
# f1 is a file handler that returns the file

# 'r' opens the file in read mode. It returns an error if the fil doesn't exist
# f1 = open('file_1', 'r')
# when the command above is run, f1 points to the start of the file

# if you want to read the file, you use the read function and store it in a variable
# data = f1.read()
# print(data)
# or run f1 = open('file_1') without the x command

# use 'w' to write something in the file. If file already exists, it overwrites it.
# If file doesn't exist, it creates a new file
# file handler exists at the beginning
# f2 = open('file_2', 'w')
# f2.write('This is the second file')
# f2.close()

# use 'r+' to open a file in read and write mode. File handler exists at the start of the file
# if file doesn't exist, it returns an error
# if you want to append a statement, you have to read the file first then write.
# If you write then read a file, the new content will begin replacing the original content
# from the beginning of the file
# the tell function tells you the index where the cursor is
# f1 = open('file_1', 'r+')
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# f1.write('This is a a python course')
# print(f1.tell())
# f1.close()

# use 'w+' to read and write mode. File handler exists at the beginning of file
# if file already exists, it overwrites the content
# if file doesn't exist, it creates a new file
# f2 = open('file_2', 'w+')
# print(f2.tell())
# f2.write('This is a python program')
# print(f2.tell())
# f2.write('Hi')
# print(f2.tell())
# when you add data to your file, the cursor moves to the end of the file
# in order to read the contents of the file in 'w+' mode, you have to move the cursor bac to the start of the file
# f2.seek(0)
# data2 = f2.read()
# print(data2)
# f2.close()

# use 'a' to append / write data
# the file handler exists at the end of the existing file
# if the file doesn't exist, it creates a new file
# f1 = open('file_1', 'a')
# f1. write('Hello')

# use 'a' to append and read
# you have to bring the file handler back to the start of the file if you want ot read the contents
f1 = open('file_1', 'a+')
f1.write('Student\n')
f1.write('Welcome')
f1.seek(0)
data = f1.read()
print(data)

# if you want to open a file that's not in the current working directory, you have to provide a file path
f3 = open('D:\\programs\\Office 2016 x64 IT 16\\Leggimi.txt', 'a+')
f3.seek(0)
print(f3.read())
