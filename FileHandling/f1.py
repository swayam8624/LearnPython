#in terminal to create a file
#command is :  touch [name of file].[type]

#for python , to open it

myfile= open('test.txt',mode='w') # or with open('test.txt') as myfile (no need to seek cursor everytime, it automatically goes to beginning)
#mode = 'r' for read , 'w' for write , 'a' for append , 'rb/wb' for read/write binary, 'r+' to read+write
print(myfile) #gives a iowrapper object
#to read 
print(myfile.read())
print(myfile.read()) # wont read anything as cursor is at end already
#to move cursor
myfile.seek(0) #pushes cursor to the beginnng
print(myfile.read())

myfile.seek(0) #pushes cursor to the beginnng
print(myfile.readline()) # reads line by line (identified by escape sequencing)
print(myfile.readline())
myfile.seek(0) 
print(myfile.readlines()) #returns list of lines

myfile.close()
