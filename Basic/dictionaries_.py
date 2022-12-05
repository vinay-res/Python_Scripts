def simple():
    dict={1:"one",2:"two",3:"three"}
    print(dict)
    print(dict)

    #printing dict
    print(dict[1])

    #changing values
    dict[1]="ONE"
    dict[4]="four"
    print(dict)

def dict_methods():
    dict={}
    #print(dir(dict))
    letters=['a','b','c','d','e']
    scores={"bob":20,"alice":23,"jim":22}
    print(scores.copy())
    scores.update({"vk":25})
    print(scores.keys())
    letterx=dict.fromkeys(letters)
    print(letterx)
    print(max(scores))
    #print(scores)
def dict_iter():
    scores={"bob":20,"alice":23,"jim":22}
    for score in scores:
        print(score)
    
    for name , score in scores:
        print(name)
        print()

    
def text_analyzer():
    """function to calculate the frequency of letters in a text"""

    text="""SimpleText is the native text editor for the Apple classic Mac OS. SimpleText 
    allows text editing and text formatting, fonts, and sizes. It was developed to integrate 
    the features included in the different versions of TeachText that were created by various 
    software development groups within Apple Computer."""
    
    #to lower all the characters
    new_text=text.lower()
    freq={}
    for char  in new_text:
        if char not in freq:
            freq[char]=1
        else:
            freq[char]+=1    

    print(freq)


    

        
        

    
#simple()    
#dict_methods()
#dict_iter()
text_analyzer()