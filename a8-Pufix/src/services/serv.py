import queue
import sys
from random import randint
import os
sys.path.insert(1, os.getcwd())
from src.domain.classes import book, client, rental

class service:
    def __init__(self,repo):
        self.repo=repo

    def pull(self):
        self.repo.load()

    def push(self):
        self.repo.save()

    def redo(self):
        self.repo.redo()

    def undo(self):
        self.repo.undo()
    def add(self,cmd):
        assert len(cmd)>1, "    add <client/book> - adds a new element"
        if cmd[0]=='book':
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
            assert len(cmd[index+1:])>0, "ERROR: Invalid command syntax"
            dictionary['author']=' '.join(cmd[index+1:])
            dictionary['uuid']= str(randint(10000000000,19999999999))[1:]
            self.repo.add(book(dictionary))
        elif cmd[0]=='client':
            cmd.pop(0)
            dictionary={}
            assert len(cmd)>0, "ERROR: Invalid command syntax"
            dictionary['name']=' '.join(cmd)
            dictionary['uuid']= str(randint(10000000000,19999999999))[1:]
            self.repo.add(client(dictionary))
        else:
            raise ValueError("ERROR: Invalid command syntax")

        return True

    def list(self, query):
        assert len(query)>0, "    list <client/book> - lists all elements"
        assert len(query)==1, "ERROR: Invalid command syntax"
        if query[0]=='books':
            self.repo.prtBooks()
        elif query[0]=='clients':
            self.repo.prtClients()
        elif query[0]=='rents':
            self.repo.prtRental()
        else:
            raise ValueError("ERROR: Invalid command syntax")
        
        

    def remove(self, query):
        assert len(query)>0, "    remove <client/book> - removes an element"
        assert len(query)>1, "ERROR: Invalid command syntax"
        if query[0]=='book':
            self.repo.removeBook(query[1:])
        elif query[0]=='client':
            self.repo.removeClient(query[1:])
        else:
            raise ValueError("ERROR: Invalid command syntax")
        
        return True

    def update(self, query):
        assert len(query)>0,"    update <client/book> <name/uuid> <name/author/uuid> <query> - updates an element"
        assert len(query)>1,"ERROR: Invalid command syntax"
        if query[0]=='book':
            self.repo.updateBook(query[1:])
        elif query[0]=='client':
            self.repo.updateClient(query[1:])
        else:
            raise ValueError("ERROR: Invalid command syntax")

        return True
        
    def rent(self,query):
        assert len(query)>0, "    rent <book> to <client> - rents a book"
        assert len(query)>1, "ERROR: Invalid command syntax"
        self.repo.rent(query)
    
    def top(self,query):
        assert len(query)>0, "    top <book/author/client> <nr_of_results> - prints the statistic"
        if len(query)==1:
            query.append(10)
        else:
            assert query[1].isdigit(), "ERROR: Invalid command syntax"
            query[1]=int(query[1])
        if query[0]=='book' or query[0]=='books':
            return self.repo.topBook(query[1])
        elif query[0]=='author' or query[0]=='authors':
            return self.repo.topAuthor(query[1])
        elif query[0]=='client' or query[0]=='clients':
            return self.repo.topClient(query[1])
        else:
            raise ValueError("ERROR: Invalid command syntax")

        
    def retrn(self,query):
        assert len(query)>0, "    return <book> from <client> - returns a book"
        assert len(query)>1, "ERROR: Invalid command syntax"
        self.repo.retrn(query)

    def search(self,query):
        assert len(query)>0, "    search <client/book> <name/uuid/author> <query> - searches for an element"
        assert len(query)>2, "ERROR: Invalid command syntax"
        if query[0]=='book':
            assert len(query)>2, "ERROR: Invalid command syntax"
            if query[1]=='name':
                return self.repo.searchBookName(" ".join(query[2:]))
            elif query[1]=='author':
                return self.repo.searchBookAuthor(" ".join(query[2:]))
            elif query[1]=='uuid':
                return self.repo.searchBookUUID(query[2])
            else:
                raise ValueError("ERROR: Invalid command syntax")
        elif query[0]=='client':
            assert len(query)>2, "ERROR: Invalid command syntax"
            if query[1]=='name':
                return self.repo.searchClientName(" ".join(query[2:]))
            elif query[1]=='uuid':
                return self.repo.searchClientUUID(query[2])
            else:
                raise ValueError("ERROR: Invalid command syntax")
        else:
            raise ValueError("ERROR: Invalid command syntax")