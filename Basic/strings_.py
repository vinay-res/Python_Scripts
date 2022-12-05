def simple():
    message1="Hello ! "
    #print(message*5)
    message2=" How are you ? "
    print(message1+message2)


def slicing():
    message1=" hello "
    print(message1[0:3],message1[-4:-1])

    message2="xyz"
    print(message2[0:],message2[-3:])

    print(len(message1),len(message2))
    #string interpolation
    print(f"The length of message1 is {len(message1)} and message2 is {len(message2)} !")
    # string formatting
    print("The length of message1 is {} and message2 is {} .".format(len(message1),len(message2)))


    
def string_methods():
    """Method to containing
      string methods usage"""
    string="hello world"
    print(string.capitalize())
    print(string.lower())
    print(string.upper())
    print(string.startswith("he"))
    print(string.endswith("l"))
    print(string.strip("el0"))
    print(string.replace("o"," "))
    print(string.split("l"))
    print(string.count("l"))

    
def escape_seq():
    """ \ new line
    \\ Backslash(\)
    \' single quote
    \\" double quote
    """

    
            

#calling all the functions
#simple()
#slicing()
string_methods()