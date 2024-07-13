#04/01/2024


#ZeroDivisionError

"""x=4
y=0
try:
 z=x/y
except ZeroDivisionError: 
  print("error occured")"""


#multiple excecpt

"""try:
 print(x)
except NameError: 
    print("variable x is not defined")
except:
    print("something else went wrong")"""



"""x=5
y=0
try:
 c=x/y
except NameError:
    print("variable c is not define")
except:
    print("something went wrong")"""
#else


"""x=5
y=0
try:
 c=x/y
except NameError:
    print("variable c is not define")
else:
    print("something went wrong")"""


#finally
x=5
try:
    print(x)
except:
       print("something went wrong")
finally:
          print("the try exdept is finished")
    

       
