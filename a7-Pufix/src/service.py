from repo import repository

class service:
    def __init__(self):
        self.repo = repository()

    def pull(self):
        self.repo.pull()
    def push(self):
        self.repo.push()
    def afis(self):
        self.repo.afis()
    def add(self,cmd):
        self.repo.add(cmd)
    def undo(self):
        self.repo.undo()
    def filter(self,cmd):
        self.repo.filter(cmd)
        

def test():
    s=service()
    s.pull()
    s.push()
    s.afis()
    s.add(['add','book','by','author'])
    assert s.repo.array[-1].name=='book'
    assert s.repo.array[-1].author=='author'
    s.undo()
    s.filter(['filter','a'])
    print("All tests passed!")
    
test()

    

