"""Type casting.

There may be times when you want to specify a type on to a variable. This can be done with casting.
Python is an object-orientated language, and as such it uses classes to define data types,
including its primitive types.

Casting in python is therefore done using constructor functions:

- int() - constructs an integer number from an integer literal, a float literal (by rounding down
to the previous whole number) literal, or a string literal (providing the string represents a
whole number)

- float() - constructs a float number from an integer literal, a float literal or a string literal
(providing the string represents a float or an integer)

- str() - constructs a string from a wide variety of data types, including strings, integer
literals and float literals
"""

a=20
b=30.99
c='5'
#Other to Int
print(int(b))
print(int(c))

#Other to Float
print(float(a))
print(float(c))

#Other to String
print(str(a))
print(str(b))
print(str(c))