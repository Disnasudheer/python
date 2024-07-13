#local scope

"""def myfunction():
    x=30
    print(x)
    
myfunction()
print(x)"""




"""def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()"""

#global scope

"""x=300

def myfunc():
    print(x)
myfunc()
print(x)"""




"""x=300

def myfunc():
    x=200
    print(x)
myfunc()
print(x)"""


#global keyword



def myfunc():
    global x
    x=300
myfunc()
print(x)
