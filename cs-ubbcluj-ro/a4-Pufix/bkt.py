def HasNeighbouringSequences(array:list): #returns true if the list HasNeighbouringSequences
    size=len(array)
    for sizeofsequence in range(1,int((size+2)/2)):
        if array[size-sizeofsequence:size]==array[size-sizeofsequence*2:size-sizeofsequence]:
            return True
    return False
def bkt(size):
    array=[-1]*size
    array[0]=0
    i=0
    while i>=0:
        array[i]+=1
        if array[i]>9:
            array[i]=-1
            i-=1
        elif HasNeighbouringSequences(array[:i+1])==False:
            if i+1==size:
                print(*array, sep="")
            else:
                i+=1
def main():
    size=int(input("Please specify how big the numbers are: "))
    bkt(size)
main()
