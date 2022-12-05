"""Program for lists"""
print(__name__)
def basic():
    letters=['a','b','c','d','e']
    numbers=[1,2,3,4,5]
    #adding lists
    print(letters+numbers)
    #multiplying lists
    print(letters*2)
    #slicing
    print(letters[0:3])
    #changing values in a list
    letters[2]=3
    print(letters)
    #appending value to the list
    letters.append("f")
    print(letters)
    
def funct():
    """function performing some list functions"""
    numbers=[1,2,3,4,5,17,54,98,32]
    print(len(numbers))
    print(max(numbers))
    print(min(numbers))
    print(sum(numbers))
    print(sorted(numbers))
    print(sorted(numbers,reverse=True))
    
def list_comp():

    squares_odd=[i**2 for i in range(1,11) if i**2 % 2 != 0]
    squares_even=[i**2 for i in range(1,11) if i**2 % 2 == 0]
    print(squares_odd,squares_even)

    
    

    

    

    
if __name__=="__main__":

    #basic()
    #funct() 
    list_comp()   