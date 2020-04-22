"""
Mostly useable list methods are
the comprehensions for all data types are same
        append*
		clear
		copy*
		count*
		extend
		index*
		insert*
		pop*
		remove
		reverse*
		sort*
"""
Fruits=["Mango","banana","apple","kiwi","waterlamon"]
Numbers=[1,5,9,3,5]
Alphabets=["A","B","C","D","E"]

Numbers.append(6)#append the value into the list
print(Numbers)
A=Alphabets.copy()#copy the one list into the new list
print(A)
print(Fruits.count("Mango"))
print(Alphabets.index("D"))#return the no of given element from list which is gotted on first occurence
Numbers.insert(2,9)#insert number on the given index
print(Numbers)
Numbers.sort()
print(Numbers)
Numbers.reverse()
print(Numbers)
Alphabets.pop(4)#pop the element which is given in index
print(Alphabets)
Fruits.remove("Mango")#same as pop remove the given element from list
print(Fruits)
if Fruits.__contains__("Mango"):#this function is case sensetive so give correct argument
    print("Contains")
else:
    print("Not Contains")
