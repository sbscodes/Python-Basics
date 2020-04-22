class FileOperation:
    def writefile(self):
        try:
            fh=open("/\\08_File Operations\\mytxt.txt", 'w')
        except FileNotFoundError:
            print("File Not Found")
        else:
            fh.write("Add this Content in file")
            print("Added Into File")

f=FileOperation()
f.writefile()