def args_funct(*args):
    total=0
    for i in args:
        total+=i

    print(total)


"""About Lambda Functions"""

#simple lambda example
add=lambda  x,y:x+y

#calculating kinetic energy (m*(v**2))/2
kinetic_energy=lambda m,v:(m*(v**2))/2

#calculating  energy e=m*(c**2)
energy=lambda m,c=3*(10**8):m*(c**2)

#lambda funct creating abbrevation from each weekday from a list

week_days=["sun","mon","tue","wed","thur","fri","sat"]

list_names=list(map(lambda week:week+"day",week_days))


#args_funct(20,10,15,1)   
#print(add(2,3)) 
#print(kinetic_energy(2,3))
#print(energy(0.0000000002))
print(list_names)