"""program on loops"""

def while_loop():
    current=1
    end=10
    while current <= end:
        print(current)
        current+=1
    else:
        print("reached the end")    


def for_loop():

    number=[1,2,3,4]
    letters=['a','b','c','d']
    l_index=0
    for n in number:
       print(str(n)+letters[l_index])
       l_index+=1
def range_funct():
    for i in range(0,10,2):
        print(i)
    
    
#while_loop()
#for_loop()    
range_funct()