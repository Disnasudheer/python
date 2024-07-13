#Reading File using ( r mode )

"""file=open("today.txt","r")
print(file.read())"""


#to getting first 2 word
"""file=open("today.txt","r")
print(file.read(2))"""

#to getting first line
"""file=open("today.txt","r")
print(file.readline())"""

#to getting first  two line 
"""file=open("today.txt","r")
print(file.readline())
print(file.readline())"""   #print 2 times to get first two line

#file open that not in the same folder of python program
"""file=open("C:/Users/saiso/Desktop/today.txt","r")
print(file.read())"""

#by using for loop
"""file=open("today.txt","r")
for each in file:
 print(each)"""

#to appending into a file use ( a mode )
"""file=open("today.txt","a")
file.write("goood")
file.close()
file=open("today.txt","r")
print(file.read())"""


#to add new content by overwrite old content use( w mode )
"""f=open("today.txt","w")
f.write("haiiii")
f.close()
f=open("today.txt","r")
print(f.read())"""



#to create a new file using python use( x mode )
f=open("myfile.txt","x")
f.write("hiii hiiihiii hiiihiii hiii hiii hiii hiii hiii hiii hiii hiii hiii hiii hiiihiii hiiihiii hiii hiii hiii hiii hiii hiii hiii hiii hiii hiii hiiihiii hiiihiii hiii hiii hiii hiii hiii hiii hiii hiii hiii hiii hiiihiii hiiihiii hiii hiii hiii hiii hiii hiii hiii hiii hiii")
f.close()
f=open("myfile.txt","r")
print(f.read())












