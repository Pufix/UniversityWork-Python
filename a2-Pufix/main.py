import random
def clean():
    for w in range(200):
        print('\n')
list=[-1]
step =1
crtstep=0
def genlist():
    n=int(input("Plese scecify how big the size is: "))
    size=len(list)
    for i in range (n):
        if i>= size:
            list.append(random.randint(1,99))
        else:
            list[i]=random.randint(1,99)
    while len(list)>n:
        list.pop()
def showstep():
    print(list)
def sort1():
    global step
    showstep()
    stepcrt=0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                c=list[i]
                list[i]=list[j]
                list[j]=c
                stepcrt+=1
                if stepcrt%step==0:
                    showstep()
                    stepcrt=0
#[92, 36, 22, 41, 32, 17, 18]
def sort2():
    global step
    global crtstep
    output=[]
    crtstep=0
    while len(list)>0:
        intermediary=[list.pop(0)]
        i=0
        while i<len(list):
            if intermediary[len(intermediary)-1]<=list[i]:
                intermediary.append(list.pop(i))
                i-=1
            i+=1
        j=0
        while len(intermediary)>0 and j<len(output):
            if intermediary[0]<=output[j]:
                output.insert(j,intermediary.pop(0))
            else:
                j+=1
        while len(intermediary)>0:
            output.append(intermediary.pop(0))
        crtstep+=1
        if crtstep%step==0:
            print(output)
            stepcrt=0
    return output
def interface():
    global list
    global step
    print("1.Generate a random list.")
    if list[0]!=-1:
        print("Curent list is:")
        print(list)
    print("2.Sort the list using Selection Sort")
    print("3.Sort the list using Strand Sort")
    print("4.Change step (current step size="+str(step)+")")
    print("0.Exit program")
    nr = int(input("Type the letter of the desired opperation followed by an enter to select it"+'\n'))
    if nr!=0:
        if nr==1:
            genlist()
            clean()
        elif nr==2:
            if list[0]!=-1:
                clean()
                sort1()
                print('\n')
            else:
                clean()
                print("Please generate list first!")
        elif nr==3:
            if list[0]!=-1:
                clean()
                list=sort2()
                print('\n')
            else:
                clean()
                print("Please generate list first!")
        elif nr==4:
            step= int(input("Please enter step size: "))
            clean()
        else:
            print("Please enter a valid number!")
        interface()
clean()
interface()
