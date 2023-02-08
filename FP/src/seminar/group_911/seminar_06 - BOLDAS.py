"""
Write an application that manages a list of circles.
Each circle has a unique center (x,y - ints) and a positive radius (int).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a circle
        - adds the given circle to the list.
        - error if circle with given center already exists, the center or radius not given, empty or radius < 0

    2. Delete a circle
        - deletes the circle with the given center
        - error if non-existing center is given

    3. Show all circles
        - shows all circles in descending order of their radius

    4. Show circles that intersect a given one
        - select a circle from the list of existing circles
        - print those which intersect it
        (bonus: sort printed circles by descending order of radius)

    5. exit
        - exit the program

    Observations:
        - Add 10 random circles at program startup
        - Write specifications for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the circle's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""

#
# Write the implementation for Seminar 06 in this file
#
import random
#
# Write below this comment
# Functions to deal with circles -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def modulus(a:int):
    if a<0:
        return a*-1
    return a
def newCircle(x:int,y:int,radius:int,array:list):
    ok=1
    for w in (array): 
        if w[0]==x and w[1]==y:
            ok=0
    if ok==1:
        array.append([x,y,radius])
    else:
        print("ERROR: the circle already exists")

def prtCircle(array:list,index:int):
    print("Circle "+str(index)+" has the coordinates: "+str(array[index][0])+" "+str(array[index][1])+" and size of : "+str(array[index][2]))

def addCircle(array:list):
    x=int(input("Please enter the X coordinate of the circle: "))
    y=int(input("Please enter the Y coordinate of the circle: "))
    size=int(input("Please enter the size of the circle: "))
    clean()
    newCircle(x,y,size,array)

def addRandCircles(array:list,nmbr:int):
    clean()
    for i in range(nmbr):
        newCircle(random.randint(-20,20),random.randint(-20,20),random.randint(1,20),array)

def prtList(array:list):
    clean()
    for i in range(len(array)):
        prtCircle(array,i)
    print()

def delCircle(array:list):
    x=int(input("Please enter the X coordinate of the circle you want to delete: "))
    y=int(input("Please enter the Y coordinate of the circle you want to delete: "))        
    ok=1
    for w in range(len(array)): 
        if array[w][0]==x and array[w][1]==y:
            ok=0
            array.pop(w)
            break
    if ok==1:
        clean()
        print("The given Circle does not exist")
        print()
    else:
        clean()
        print("Circle succesfully deleted")
        print()

def CircOverlap(array):
    x=int(input("Please enter the X coordinate of the circle you want to use: "))
    y=int(input("Please enter the Y coordinate of the circle you want to use: "))        
    ok=0
    i=0
    for w in range(len(array)): 
        if array[w][0]==x and array[w][1]==y:
            ok=1
            i=w
            break
    if ok==0:
        clean()
        print("The given Circle does not exist")
        print()
    else:
        clean()
        goodlist=[]
        for w in range(len(array)):
            #calculationg Pytagora's theorem
            distanceOrigin= modulus(array[w][0]-array[i][0])*modulus(array[w][0]-array[i][0])
            distanceOrigin+= modulus(array[w][1]-array[i][1])*modulus(array[w][1]-array[i][1])
            distanceDiameters=(array[w][2]+array[i][2])*(array[w][2]+array[i][2])
            if distanceDiameters>=distanceOrigin and w!=i:
                goodlist.append(array[w])
        if len(goodlist)==0:
            print("Didnt find no intersections")
        else:
            prtList(goodlist)
            print("This is the list of circles that intersect"+str(array[w]))

#
# Write below this comment
# Functions to deal with circles -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#
# Write below this comment
# Functions that deal with the required functionalities properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def clean():
    for ww in range(300):
        print()

def prtmenu():
    menuoptions="""
1.Show current list of Circles
2.Add a specific Circle to the list
3.Add some random Cicles to the list
4.Delete a circle of the list
5.Show the Circles that intersect a given Circle
0.EXIT
"""
    print(menuoptions)

def runtime(array:list):
    prtmenu()
    option=int(input("Please enter what option do you want to use: "))
    if option!=0:
        if option==1:
            prtList(array)
        elif option==2:
            addCircle(array)
        elif option==3:
            nr=int(input("Please enter how many random cirles do you want to add: "))
            addRandCircles(array,nr)
        elif option==4:
            delCircle(array)
        elif option==5:
            CircOverlap(array)
        else:
            clean()
            print("ERROR: invalid operation")
            print()
        runtime(array)

def main():
    array=[]
    addRandCircles(array,10)
    clean()
    runtime(array)
main()