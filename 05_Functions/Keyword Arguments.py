def kwargs(color ,bird='parrot' ,lives='tree' ,fly='sky'):
    print("the name of bird is %s"% bird)
    print("the color of %s is %s"%(bird,color))
    print("the %s lives on %s"%(bird,lives))
    print("the %s is wondering at %s"%(bird,fly))

#kwargs("green")#one positional argument
#kwargs(color="brown" ,bird="Sparrow")#2 keyword argument
#kwargs("voilet","gilhari") #2 postional argumetns
kwargs("rainbow","peocock","land","not fly")#all positional
kwargs(color="brown" ,bird="eagle" ,lives="mountains" ,fly="above the sky")#all keyword
