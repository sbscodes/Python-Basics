fh=open("/\\08_File Operations\\mytxt.txt", 'r+')

print(fh.seek(7))#place the file cursor at the given position
print(fh.tell())#return the postion of the cursor of the file
print(fh.flush())#flush the file contents
print(fh.encoding)#return the encoding of file
print(fh.errors)#returns errors of file
print(fh.mode)#returns in which mode file is opened
print(fh.name)#return the file name means total path of given to open
print(fh.writable())#check whether writeable or not
print(fh.seekable())#check whether seekable or not
print(fh.readable())#check wheter readable or not
str="This is first line"
fh.writelines(str)#write myltiple lines in the file
print(fh.newlines)#return the new added lines into the file
print("Readline is"+fh.readline(1))#read the charecters of the given limit
print(fh.readlines())#read the complete line of the file
a=fh.__sizeof__()
fh.truncate(a)
print(fh.readlines())
fh.close()#close the file object
print(fh.closed)#check whether file is closed or not