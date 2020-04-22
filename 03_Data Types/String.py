#Strings in python and all it's method with comprehesions
String=" HelLo This is a String"
String1="Hello  World"
String2="live like king like me"

print(String2[5]) #print value of string of given index(Which is start from 0)
print(String[:]) #print all values in String we can also give only string name
print(String[:2])#from first upto number
print(String1[4:])#from last upto number
print(String1+String)#String concatenation using '+' Operator
print(String2*2)
strr="Jumanji:Welcome to the Jungle"
print(String2.capitalize())#capitalize first letter of string
print(String.casefold())#return string in small letters
#print(String.center(5,"l"))
print(String.count("e"))#count the total no of occurence of char in string
#print(strr.endswith())
print(String1.expandtabs(20))
print(strr.find("e",20,28))#return the first occerence of letter in string
print("{0}=Movie".format(strr))#returm string in {} which get refered as tuple
print(strr.format_map(11))
print(String2.index("l"))#returns first occurence of word