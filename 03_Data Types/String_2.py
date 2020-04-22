str="ABCDEF"
strr2="12345"
print(str.join(strr2))

strr="Hello User Hello Hello"
print(strr.lstrip("Hello"))#strip the string which is passed from main string
print(strr.ljust(2,'E'))
print(strr.lower())
print(strr.split(" ",2))
print(strr.strip("str"))
print(strr.replace("Hello",str,2)) #last parameter is for how many times do you want to replace
print(strr.startswith("Hello",0,10))
print(strr.swapcase())
print(strr.zfill(100))#fills character above the string length with zeros