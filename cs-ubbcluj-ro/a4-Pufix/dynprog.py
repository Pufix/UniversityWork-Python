def sort(array:list):
    if len(array)>1:
        right=array[int(len(array)/2):]
        left=array[:int(len(array)/2)]
        sort(left)
        sort(right)
        i = 0
        j = 0
        for l in range(len(array)):
            if i<len(left) and j<len(right):
                if left[i]<right[j]:
                    array[l]=left[i]
                    i+=1
                else:
                    array[l]=right[j]
                    j+=1
            elif i<len(left):
                array[l]=left[i]
                i+=1
            else:
                array[l]=right[j]
                j+=1
def subsets(array:list):
    sum=0
    for i in array:
        sum+=i
    sumpart=[False]*int(sum/2+1)
    sumpart[0]=True
    lastadd=[-1]*int(sum/2+1)
    for i in range(len(array)):
        for j in range(int(sum/2+1),-1,-1):
            if array[i]+j<=sum/2 and sumpart[j]==True:
                sumpart[j+array[i]]=True
                lastadd[j+array[i]]=i
    if sumpart[-1]:
        solution=[]
        i = int(sum/2)
        while i>0:
            solution.append(array.pop(lastadd[i]))
            i-=solution[-1]
        print(solution,end="")
        print(" + ",end="")
        print(array)
    else:
        print("Not possible")
def main():
    array=[int(item) for item in input("Enter the list items : ").split()]
    sort(array)
    subsets(array)

main()