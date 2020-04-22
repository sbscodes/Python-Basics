#here we are passed the list directly into function
#or passed the seperataly created list to the function

def funarg(*args):#here arguments are in the form of tuple or list
    for b in args:
        print(b)
tup=("2","prafull","1999","KTHM","TYBSC")
funarg(*tup)
funarg("1","Viraj","2000","TCS","TYBSC")

#here we are passed the whole dictionary to the function
def funkwarg(**kwargs):#here the arguments are in the form of dictionary
    for a,b in kwargs.items():
        print(a+" : "+b)

di={"Roll No":'1',"NAME":"viraj","BirthYear":'2000',"Company":'TCS',"Class":"TYBSC"}
funkwarg(**di)

#here we are passed the only values of dictionary to the function

def names_arguments(first, last):
    return first + ' ' + last +'!'


names= {'first': 'Satish', 'last': 'Birhade'}
names_arguments(**names)