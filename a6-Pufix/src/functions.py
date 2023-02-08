#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import random
currentList=[]
oldLists=[]

def modPeeps(index,prob,value):
    oldLists.append(currentList.copy())
    if prob=='p1':
        currentList[index][0]=value
    if prob=='p2':
        currentList[index][1]=value
    if prob=='p3':
        currentList[index][2]=value

def remove(start,fin):
    oldLists.append(currentList.copy())
    for index in range(start,fin+1):
        currentList.pop(start)

def getList():
    global currentList
    return currentList

def delOld():
    global oldLists
    oldLists.pop()

def addNewPeeps(p1,p2,p3,pos):
    oldLists.append(currentList.copy())
    if pos==-1:
        currentList.append([p1,p2,p3])
    else:
        currentList.insert(pos,[p1,p2,p3])

def initialization(nbr:int):
    for counter in range(nbr):
        addNewPeeps(random.randint(0,10),random.randint(0,10),random.randint(0,10),-1)

def undoAction(): 
    global currentList
    if len(oldLists)==0:
        raise ValueError('ERROR: There is nothing to undo!')
    else:
        currentList=oldLists.pop()

