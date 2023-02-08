#
# Write the implementation for A5 in this file
#
import math
import re
import random
from venv import create
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

def createnr(a:int,b:int):
    return {"real": a, "img": b}
def getreal(c):
   return c["real"]
def getimg(c):
   return c["img"]


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def isprime(x:int):
    if x==1 or x ==0:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    i=3
    while i*i<=x:
        if x%i==0:
            return False
        i+=2
    return True

def modulo(nr):
    a=int(getreal(nr))
    b=int(getimg(nr))
    return math.sqrt(a*a+b*b)

def aplication(array:list):
    maxi=0
    leng=[0]*len(array)
    for i in range(1,len(leng)):
        if isprime(int(modulo(array[i])-modulo(array[i-1]))):
            leng[i]=leng[i-1]+1
            if leng[i]>leng[maxi]:
                maxi=i
    if maxi>0:
        print("length= "+str(leng[maxi]+1))
        prtlist(array[maxi-leng[maxi]:maxi+1])
    else:
        print("There isn't a suitable subarray")

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
3.Find length and elements of a longest subarray of numbers where the difference between the modulus of consecutive numbers is a prime number.
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
    array.append(createnr(-5,0))
    array.append(createnr(0,8))
    array.append(createnr(12,5))
    for i in range(10):
        array.append(createnr(random.randint(-20,20),random.randint(-20,20)))
    run=True
    clean()
    while run:
        run=runtime(array)
main()



