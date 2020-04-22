with open('/\\08_File Operations\\mytxt.txt', 'r') as f:
    print(f.readline())

print(f.closed)#with function automatically closed the file afeter work done

