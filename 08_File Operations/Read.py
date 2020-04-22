class FileOperation:
    def readfile(self):
        try:
            fh=open("/\\08_File Operations\\mytxt.txt", 'r')
        except FileNotFoundError:
            print("File Not Found")
        else:
            print("Contents Of file are")
            print(fh.read())

f=FileOperation()
f.readfile()