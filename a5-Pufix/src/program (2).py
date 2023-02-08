#
# Write the implementation for A5 in this file
#
from asyncio.windows_events import NULL
import math
import re
import random
# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
#def getreal(c:list):
#    return c[0]
#def getimg(c:list):
#    return c[1]
#def createnr(a:int,b:int):
#    return [a,b]


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def getreal(c):
   return c["real"]
def getimg(c):
   return c["img"]
def createnr(a:int,b:int):
    return {"real": a, "img": b}

#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def aplication(array:list):
    maxl=1
    last=getreal(array[0])
    last2=getreal(array[0])
    sense=1
    max2=1
    sense2=-1
    sol1=[array[0]]
    sol2=[array[0]]
    for i in (array[1:]):
        if sense==1:
            if getreal(i)>last:
                sol1.append(i)
                maxl+=1
                last=getreal(i)
                sense*=-1
            else:
                sol1.pop()
                sol1.append(i)
                last=getreal(i)
        else:
            if getreal(i)<last:
                maxl+=1
                last=getreal(i)
                sense*=-1
                sol1.append(i)
            else:
                sol1.pop()
                sol1.append(i)
                last=getreal(i)
        if sense2==1:
            if getreal(i)>last2:
                max2+=1
                last2=getreal(i)
                sense2*=-1
                sol2.append(i)
            else:
                sol2.pop()
                sol2.append(i)
                last2=getreal(i)
        else:
            if getreal(i)<last2:
                max2+=1
                last2=getreal(i)
                sense2*=-1
                sol2.append(i)
            else:
                sol2.pop()
                sol2.append(i)
                last2=getreal(i)
    if max2>maxl:
        print(max2)
        print()
        prtlist(sol2)
    else:
        print(maxl)
        print()
        prtlist(sol1)



#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def prtnmbr(nr):
    a=int(getreal(nr))
    b=int(getimg(nr))
    if b==0:
        print(a)
    elif a==0:
        if b==1:
            print("i")
        elif b==-1:
            print("-i")
        else:
            print(str(b)+"i")
    elif b>0:
        if b!=1:
            print(str(a)+"+"+str(b)+"i")
        else:
            print(str(a)+"+i")
    else:
        if b!=-1:
            print(str(a)+str(b)+"i")
        else:
            print(str(a)+"-i")

def clean():
    w=200
    while w>0:
        print()
        w-=1
def prtlist(array:list):
    for i in array:
        prtnmbr(i)

def prtmenu():
    menu="""
1.Show list of numbers
2.Add a number to the list
3.Find The length and elements of a longest alternating subsequence, when considering each number's real part.
0.EXIT
"""
    print(menu)

def read(array:list):
    nbr=input("Please enter the number you want to add: ")
    numbers=re.findall(r'\d+', nbr)
    if len(numbers)==1:
        if nbr.find('-')==0:
            numbers[0]='-'+numbers[0]
        if nbr.find('+i')>0:
            array.append(createnr(numbers[0],1))
        elif nbr.find('-i')>0:
            array.append(createnr(numbers[0],-1))
        elif nbr.find('i')>0:
            array.append(createnr(0,numbers[0]))
        else:
            array.append(createnr(numbers[0],0))
    elif len(numbers)==2:
        if nbr.find('-')==0:
            numbers[0]='-'+numbers[0]
        if nbr[1:].find('-')>0:
            array.append(createnr(numbers[0],'-'+numbers[1]))
        else:
            array.append(createnr(numbers[0],numbers[1]))
    else:
        if nbr.find('-')==0:
            array.append(createnr(0,-1))
        else:
            array.append(createnr(0,1))

def runtime(array:list):
    prtmenu()
    n=int(input("Please select your desired option: "))
    if n==0:
        return False
    if n==1:
        clean()
        prtlist(array)
        print()
        return True
    if n==2:
        print("\n\n")
        read(array)
        clean()
        return True
    if n==3:
        clean()
        aplication(array)
        return True
    return False

def main():
    array=[]
    array.append(createnr(-2,1))
    array.append(createnr(0,1))
    array.append(createnr(0,-1))
    array.append(createnr(1,7))
    array.append(createnr(3,8))
    array.append(createnr(2,8))
    array.append(createnr(4,8))
    array.append(createnr(10,8))
    array.append(createnr(6,8))
    array.append(createnr(1,8))
    for i in range(10):
        array.append(createnr(random.randint(-20,20),random.randint(-20,20)))
    run=True
    clean()
    while run:
        run=runtime(array)
main()



