def Stringfunc(strr):


    if strr.isalnum():
        print("String is alphanumeric")
    else:
        print("String is not alphanumeric")

    if strr.isalpha():
        print("String is alphabets")
    else:
        print("String is not alphabets")

    if strr.isdecimal():
        print("String is Decimal")
    else:
        print("String is not Decimal")

    if strr.isdigit():
        print("String is digit ")
    else:
        print("String is not digit")

    if strr.isidentifier():
        print("String is identifier")
    else:
        print("String is not identifier")

    if strr.islower():
        print("String is lower")
    else:
        print("String is not not lower")

    if strr.isnumeric():
        print("String is numeric")
    else:
        print("String is not numeric")

    if strr.isprintable():
        print("String is printable")
    else:
        print("String is not printable")

    if strr.isspace():
        print("String is space")
    else:
        print("String is not space")

    if strr.istitle():
        print("String is title")
    else:
        print("String is not title")

    if strr.isupper():
        print("String is uppercase")
    else:
        print("String is not uppercase")


strr="Enter any String Do you want to check these all 11 String functions "
Stringfunc(strr)