import random
import time
def clean():#cleans the console
    for w in range(200):
        print('\n')
list=[-1]
step =1
crtstep=0
def genworst(n):#generates a descending list of size N, worst case scenario
    size=len(list)
    for i in range (n):
        if i>= size:
            list.append(n-i)
        else:
            list[i]=n-i
    while len(list)>n:
        list.pop()
def genbest(n):#generates an ascending list of size N, best case scenario
    size=len(list)
    for i in range (n):
        if i>= size:
            list.append(i)
        else:
            list[i]=i
    while len(list)>n:
        list.pop()
def genrand(n):#generates a random list of N elements, used for average case
    size=len(list)
    for i in range (n):
        if i>= size:
            list.append(random.randint(1,10000))
        else:
            list[i]=random.randint(1,10000)
    while len(list)>n:
        list.pop()
def sort1(): #Selection Sort(Two For search)
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                c=list[i]
                list[i]=list[j]
                list[j]=c

def sort2(mylist):#Merge Sort
    if len(mylist)>1:
        mid=int(len(mylist)/2)
        left=mylist[:mid]
        right=mylist[mid:]
        sort2(left)
        sort2(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                mylist[k]=left[i]
                i+=1
            else:
                mylist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            mylist[k]=left[i]
            i+=1
            k+=1    
        while j<len(right):
            mylist[k]=right[j]
            j+=1
            k+=1
def sort3(mylist):
    output=[]
    crtstep=0
    while len(mylist)>0:
        intermediary=[mylist.pop(0)]
        i=0
        while i<len(mylist):
            if intermediary[len(intermediary)-1]<=mylist[i]:
                intermediary.append(mylist.pop(i))
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
    global list
    list=output
def genoption(n,size):#picks which scenario will be used for testing
    if n==4:
        genworst(size)
    elif n==5:
        genbest(size)
    else:
        genrand(size)
def sort(alg):#picks which sorting algorithm will be used for testing
    global list
    if alg==1:
        sort1()
    elif alg==2:
        sort2(list)
    else:
        sort3(list)
def interface(): #prints out an interface for the user to use
    global list
    print("1.Generate a random list.")
    if list[0]!=-1:
        print("Curent list is:")
        print(list)
    print("2.Sort the list using 2 For Sorting")
    print("3.Sort the list using Merge Sort")
    print("4.Time worst case scenario")
    print("5.Time best case scenario")
    print("6.Time average case scenario")
    print("0.Exit program")
    nr = int(input("Type the letter of the desired opperation followed by an enter to select it"+'\n'))
    if nr!=0:# nr represents the option that the user picked 
        if nr==1:# legacy from A2 - generates a random list
            size=int(input("Plese spotify how big the size is: "))
            genrand(size)
            clean()
        elif nr==2:# legacy from A2 - sorts the random list with Selection Sort
            if list[0]!=-1:
                clean()
                sort1()
                print('\n')
            else:
                clean()
                print("Please generate list first!")
        elif nr==3:# legacy from A2 - sorts the random list with Merge Sort
            if list[0]!=-1:
                clean()
                sort2(list)
            else:
                clean()
                print("Please generate list first!")
        elif nr==4 or nr==5 or nr ==6: #Time testing for the algorithms
            print("\n\n 1->Selection Sort     2-> Merge Sort    3->Strand Sort")
            alg= int(input("Please select what sorting algorithm will be used:"))
            clean()
            if alg!=1 and alg!=2 and alg!=3:
                print("Please enter valid options!")
            else:
                print("Times:")
                genoption(nr,500)
                starttime=time.time()
                sort(alg)
                time500= time.time()-starttime
                print("For 500 numbers it took  %s seconds" % (time500))
                genoption(nr,1000)
                starttime=time.time()
                sort(alg)
                time1000= time.time()-starttime
                print("For 1000 numbers it took  %s seconds" % (time1000))
                genoption(nr,2000)
                starttime=time.time()
                sort(alg)
                time2000= time.time()-starttime
                print("For 2000 numbers it took  %s seconds" % (time2000))
                genoption(nr,4000)
                starttime=time.time()
                sort(alg)
                time4000= time.time()-starttime
                print("For 4000 numbers it took  %s seconds" % (time4000))
                genoption(nr,8000)
                starttime=time.time()
                sort(alg)
                time8000= time.time()-starttime
                print("For 8000 numbers it took  %s seconds" % (time8000))
                if alg==2:
                    genoption(nr,16000)
                    starttime=time.time()
                    sort(alg)
                    timp=time.time()-starttime
                    print("For 16000 numbers it took  %s seconds" % (timp))
                    genoption(nr,32000)
                    starttime=time.time()
                    sort(alg)
                    timp=time.time()-starttime
                    print("For 32000 numbers it took  %s seconds" % (timp))
                    genoption(nr,64000)
                    starttime=time.time()
                    sort(alg)
                    timp=time.time()-starttime
                    print("For 64000 numbers it took  %s seconds" % (timp))
                print("\n\n\n\n\n\n")
                list[0]=-1
        else:
            print("Please enter a valid number!")
        interface()
clean()
interface()
