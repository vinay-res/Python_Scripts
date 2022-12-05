"""program on Map and Filter"""

def triple(value):
    return value*3

def quadraple(a_list):
    res_list=(map(lambda value:value*4,a_list))
    return res_list


def triple_stuff():
    res_list=(map(triple,{1:2,2:3}))
    return res_list


list1=[1,2,3,4]
res=list(triple_stuff())
res2=quadraple(list1)
print(res)
print(res2)
#print(triple_stuff(list1))
#print(quadraple(list1))    
                
    