"""
Mainly used dictionary methods are
        clear*
		copy*
		fromkeys**
		get*
		items*
		keys*
		pop*
		popitem*
		setdefault*#append the value passed as argument
		update**
		values*

"""

dictionary={"A":"apple",1:"One","B":"ball",2:"two"}

print(dictionary.keys())
print(dictionary.values())

for keys,values in dictionary.items():
    print(keys,values)

c=dictionary.get("A")
print(c)
print(dictionary.popitem())
print(dictionary.pop("A"))
dictionary.setdefault("A","Ambrella")
print(dictionary)
d =dictionary.copy()
print(d)
d.clear()
dictionary.clear()
print(d)
print(dictionary)