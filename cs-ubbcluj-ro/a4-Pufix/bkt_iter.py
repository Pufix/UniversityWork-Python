def HasNeighbouringSequences(array:list): #returns true if the list HasNeighbouringSequences
    size=len(array)
    for sizeofsequence in range(1,int((size+2)/2)):
        if array[size-sizeofsequence:size]==array[size-sizeofsequence*2:size-sizeofsequence]:
            return True
    return False
maxsize=int(input("Please specify how big the numbers are: "))
array=[0]*maxsize
def numbergen(pos:int,array:list):
    for i in range(10):
        if pos>0 or i >0:
            array[pos]=i
            if HasNeighbouringSequences(array[:pos+1])==False:
                if pos==maxsize-1:
                    print(*array, sep="")
                else:
                    numbergen(pos+1,array)
numbergen(0,array)

