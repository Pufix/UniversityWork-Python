#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import functions

def helpmenu():
    helpmen="""
add <P1 score> <P2 score> <P3 score> 
insert <P1 score> <P2 score> <P3 score> at <position>
remove <position>
remove <start position> to <end position>
replace <old score> <p1 | p2 | p3> with <new score>
list
list sorted
list [ < | = | > ] <score>
top <number>
top <number> <p1 | p2 | p3>
remove [ < | = | > ] <score>
undo
quit/exit"""
    print(helpmen)

def mainmenu():
    menu="""
Greeting and wellcome to the 2022 International Mathematical Olympiad
This is the program that keeps track of the student's result for day one

Use help for a list of commands

Please enter what command do you want to execute: 


"""
    print(menu)

def getCmd():
    cmd=input()
    command=cmd.split()
    cmdList=[
        "exit",
        "quit",
        "ragequit",
        "undo",
        "list",
        "add",
        "insert",
        "top",
        "remove",
        "replace",
        "help",
        ]
    ok=0
    for trycmd in cmdList:
        if trycmd == command[0]:
            ok=1
            break
    if ok==0:
        raise ValueError("ERROR: Invalid command!")
    return command

def addingPeeps(cmd:list):
    try:
        if len(cmd)<3:
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[1].isnumeric() and cmd[2].isnumeric() and cmd[3].isnumeric():
            cmd[1]=int(cmd[1])
            cmd[2]=int(cmd[2])
            cmd[3]=int(cmd[3])
            if cmd[1]<0 or cmd[2]<0 or cmd[3]<0 or cmd[1]>10 or cmd[2]>10 or cmd[3]>10:
                raise ValueError("ERROR: Invalid command syntax!")
            if cmd[0]=='insert':
                if len(cmd)<5:
                    raise ValueError("ERROR: Invalid command syntax!")  
                if cmd[4]!='at':
                    raise ValueError("ERROR: Invalid command syntax!")
                if cmd[5].isnumeric()==False:
                    raise ValueError("ERROR: Invalid command syntax!")
                else:
                    if int(cmd[5])>=len(functions.getList()):
                        raise ValueError("ERROR: Invalid insert position")
                    functions.addNewPeeps(cmd[1],cmd[2],cmd[3],int(cmd[5]))
            else:
                functions.addNewPeeps(cmd[1],cmd[2],cmd[3],-1)
        else:
            raise ValueError("ERROR: Invalid command syntax!")
    except ValueError as err:
        print(err)

def problem1(mylist:list):
    return mylist[0]
def problem2(mylist:list):
    return mylist[1]
def problem3(mylist:list):
    return mylist[2]

def podium(cmd:list):
    try:
        if len(cmd)==1:
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[1].isnumeric()==False:
            raise ValueError("ERROR: Invalid command syntax!")
        if len(cmd)==2:
            crtlist=functions.getList().copy()
            if int(cmd[1])>=len(crtlist):
                raise ValueError("ERROR: Too many contestants")
            crtlist.sort(reverse=True,key=avgscore)
            prtList(crtlist[:int(cmd[1])])
        elif len(cmd)==3:
            if cmd[2]=='p1' or cmd[2]== 'p2' or cmd[2]== 'p3':
                crtlist=functions.getList().copy()
                if int(cmd[1])>len(crtlist):
                    raise ValueError("ERROR: Too many contestants")
                if cmd[2]=='p1':
                    crtlist.sort(reverse=True,key=problem1)
                elif cmd[2]=='p2':
                    crtlist.sort(reverse=True,key=problem2)
                elif cmd[2]=='p3':
                    crtlist.sort(reverse=True,key=problem3)
                prtList(crtlist[:int(cmd[1])])
            else:
                raise ValueError("ERROR: Invalid command syntax")
        else:
            raise ValueError("ERROR: Invalid command syntax!")
    except ValueError as err:
        print(err)

def removal(cmd:list):
    try:
        if len(cmd)==1:
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[1].isnumeric()==False and not (cmd[1] in ['>','<','=']):
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[1].isnumeric():
            if len(cmd)==3:
                raise ValueError("ERROR: Invalid command syntax!")
            if len(cmd)==4 and cmd[3].isnumeric()==False:
                raise ValueError("ERROR: Invalid command syntax!")
            if len(cmd)==4 and cmd[2]!='to':
                raise ValueError("ERROR: Invalid command syntax!")
            if len(cmd)==2:
                functions.remove(int(cmd[1]),int(cmd[1]))
            else:
                functions.remove(int(cmd[1]),int(cmd[3]))
        else:
            if len(cmd)==2:
                raise ValueError("ERROR: Invalid command syntax!")
            if cmd[2].isnumeric()==False:
                raise ValueError("ERROR: Invalid command syntax!")
            if cmd[1]=='<':
                crtlist=functions.getList().copy()
                index=len(crtlist)-1
                while index >= 0:
                    if avgscore(crtlist[index])<int(cmd[2]):
                        functions.remove(index,index)
                    index-=1
                for index in range(2,len(crtlist)):
                    functions.delOld()
            elif cmd[1]=='>':
                crtlist=functions.getList().copy()
                index=len(crtlist)-1
                while index >= 0:
                    if avgscore(crtlist[index])>int(cmd[2]):
                        functions.remove(index,index)
                    index-=1
                for index in range(2,len(crtlist)):
                    functions.delOld()
            else:
                crtlist=functions.getList().copy()
                index=len(crtlist)-1
                while index >= 0:
                    if avgscore(crtlist[index])==int(cmd[2]):
                        functions.remove(index,index)
                    index-=1
                for index in range(2,len(crtlist)):
                    functions.delOld()
    except ValueError as err:
        print(err)

def replacing(cmd):
    try:
        if len(cmd)!=5:
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[1].isnumeric()==False:
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[2] in ['p1','p2','p3'] == False:
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[3]!='with':
            raise ValueError("ERROR: Invalid command syntax!")
        if cmd[4].isnumeric()==False:
            raise ValueError("ERROR: Invalid command syntax!")
        if int(cmd[4])<0 or int(cmd[4])>10:
            raise ValueError("ERROR: Invalid command syntax!")
        functions.modPeeps(int(cmd[1]),cmd[2],int(cmd[4]))
    except ValueError as err:
        print(err)

def runtime():
    try:
        cmd=getCmd()
        if cmd[0]=='exit' or cmd[0]=='quit' or cmd[0]=='ragequit':
            return False
        if cmd[0]=='undo':
            undoAct()
        if cmd[0]=='list':
            display(cmd)
        if cmd[0]=='add' or cmd[0]=='insert':
            addingPeeps(cmd)
        if cmd[0]=='top':
            podium(cmd)
        if cmd[0]=='remove':
            removal(cmd)
        if cmd[0]=='replace':
            replacing(cmd)
        if cmd[0]=='help':
            helpmenu()

        print('\n')
    except ValueError as err:
        print(err)
    return True

def startUp():
    functions.initialization(11)
    mainmenu()
    run = True
    while run:
        run=runtime()

def undoAct():
    try:
        functions.undoAction()
    except ValueError as err:
        print(err)

def prtList(crtlist:list):
    print("The results are: ")
    for index in range(len(crtlist)):
        print(crtlist[index])

def avgscore(grades:list):
    avg=grades[0]+grades[1]+grades[2]
    return avg/3

def display(cmd:list):
    crtlist=functions.getList().copy()
    try:
        if len(cmd)==1:
            prtList(crtlist)
        elif len(cmd)==2 and cmd[1]=='sorted':
            crtlist.sort(reverse=True,key=avgscore)
            prtList(crtlist)
        elif len(cmd)==3 and (cmd[1]=='<' or cmd[1]=='>' or cmd[1]=='=') and cmd[2].isnumeric() and int(cmd[2])>=0 and int(cmd[2])<=10:
            cmd[2]=float(cmd[2])
            if cmd[1]=='<':
                crt=0
                while crt<len(crtlist):
                    if avgscore(crtlist[crt])>=cmd[2]:
                        crtlist.pop(crt)
                    else:
                        crt+=1
            elif cmd[1]=='>':
                crt=0
                while crt<len(crtlist):
                    if avgscore(crtlist[crt])<=cmd[2]:
                        crtlist.pop(crt)
                    else:
                        crt+=1
            else:
                crt=0
                while crt<len(crtlist):
                    if avgscore(crtlist[crt])!=cmd[2]:
                        crtlist.pop(crt)
                    else:
                        crt+=1
            prtList(crtlist)
        else:
            raise ValueError("ERROR:syntax invalid!")
    except ValueError as err:
        print(err)



