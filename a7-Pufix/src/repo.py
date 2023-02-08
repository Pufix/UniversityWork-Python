from inbound import pull_db 
from outbound import push_db
from domain import book
from random import randint


class repository:
    def __init__(self):
        self.pull()
        self.modifications=[]
        
    def pull(self):
        self.array=pull_db()

    def push(self):
        push_db(self.array,self.modifications)

    def afis(self):
        for bok in self.array:
            bok.prt()
            print()

    def add(self,cmd):
        cmd.pop(0)
        index=0
        for i in reversed(range(len(cmd))):
            if cmd[i] == 'by':
                index=i
                break 
        if index==0:
            raise ValueError("ERROR: Invalid command syntax")
        dictionary={}
        dictionary['name']=' '.join(cmd[:index])
        dictionary['author']=' '.join(cmd[index+1:])
        dictionary['uuid']= str(randint(10000000000,19999999999))[1:]
        self.array.append(book(dictionary))
        self.modifications.append(['add',len(self.array)-1])

    def undo(self):
        assert len(self.modifications)!=0, "ERROR: There is nothing to undo!"
        if self.modifications[-1][0]=='add':
            self.array.pop(self.modifications[-1][1])
        elif self.modifications[-1][0]=='filter':
            for i in reversed(self.modifications[-1][1]):
                self.array.insert(i[1],i[0])
        self.modifications.pop()
            

    def filter(self,cmd):
        cmd.pop(0)
        assert len(cmd)==1 ,"ERROR: Invalid command syntax"
        assert len(cmd[0])==1 ,"ERROR: Invalid command syntax"
        assert cmd[0][0]>='a' and cmd[0][0]<='z',"ERROR: Invalid command syntax"
        deleted=[]
        i=0
        while i <len(self.array):
            if self.array[i].get_first_letter()==cmd[0][0] or self.array[i].get_first_letter().capitalize()==cmd[0][0] or self.array[i].get_first_letter().lower()==cmd[0][0]:
                deleted.append([self.array.pop(i),i])
            else:
                i+=1
        assert len(deleted)!=0, "Nothing was filtered out"
        self.modifications.append(['filter',deleted])

        

def test():
    repo=repository()
    repo.add(['add','The','Lord','of','the','Rings','by','J.R.R','Tolkien'])
    assert repo.array[-1].author=='J.R.R Tolkien'
    assert repo.array[-1].name=='The Lord of the Rings'

    repo.filter(['filter','t'])
    assert repo.array[-1].author!='J.R.R Tolkien'
    assert repo.array[-1].name!='The Lord of the Rings'
    repo.undo()
    assert repo.array[-1].author=='J.R.R Tolkien'
    assert repo.array[-1].name=='The Lord of the Rings'
    print("All tests passed!")
test()
   


        