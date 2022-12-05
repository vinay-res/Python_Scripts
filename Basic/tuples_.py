"""Program about tuples operations"""
def simple():
    pets=("cat","dog","horse")
    wild=("lion","zebra","antelope")
    animals=pets+wild
    print(animals)
    #2d tuple
    twod=((1,2),(2,3),(3,4))
    a,b,c=twod
    print(a[0],b[0],c[0])
    print(pets.count("dog"))
    
    print(max(pets))



def pack_unpack():
    #packing tuple
    pack=1,"hi",3
    print(pack)
    #unpacking tuple
    a,b,c=pack
    print(a,b,c)

def tuple_comp():
    squares=tuple([i**2 for i in range(1,10)])
    print(squares)
            


simple()    
#pack_unpack()    
#tuple_comp()