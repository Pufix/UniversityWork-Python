class book:
    def __init__(self,dict):
        self.uuid = dict['uuid']
        self.name = dict['name']
        self.author = dict['author']

    def prt(self):
        print("Book#"+str(self.uuid)+" is "+str(self.name)+" by "+str(self.author))

    def get_first_letter(self):
        return self.name[0]