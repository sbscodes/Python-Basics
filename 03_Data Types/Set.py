"""
Mostly using set methods are
    add*
		clear*
		copy*
		difference*
		discard*
		intersection*
		isdisjoint*
		issubset*
		issuperset*
		pop*
		remove*
		symmetric_difference*
		union*
		update*
"""
s={"Fruits","books",3,5,8,"Digit","Alphbets","rahul","pradip","Vegetables"}
ss={"Fruits","books",3,5,8,"Digit","Alphbets","Vegetables"}

s.add("Veg")
print(s)
print(s.difference(ss))#return the elements which are not same in list
print(s.intersection(ss))#returns the elements which are same
print(s.symmetric_difference(ss))
print(s.union(ss))#unions the 2 or more set and avoid duplication
s.discard("Alphbets")#discard the element from the set
print(s)
print(s.issubset(ss))
print(s.issuperset(ss))
print(ss.isdisjoint(s))
s.pop()
print(s)
ss.remove("books")
print(ss)
s.clear()
ss.clear()
print(s,ss)