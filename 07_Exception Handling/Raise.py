a=[1,2,3,4,5]

try:
    if(len(a)==7):
        print(len(a))
    else:
        raise IndexError("Your enterd Extra length")

finally:print("This block can execute anyway")