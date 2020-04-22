a=0
while a<3:
    print("while loop times")
    a+=1
else:#we can add else statement to while loop in python it shows where loop ends
    print("Printing Ended")

#multiplication table
a=2
b=1
i=0
while i<10:
    print("Multiplication is {0}*{1}={2}".format(a,b,a*b))
    b+=1
    i+=1
else:
    print("Multiplication Ended")