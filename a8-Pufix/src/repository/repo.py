from asyncio.windows_events import NULL
from copy import copy, deepcopy
import json
import os
from random import randint
import sys
sys.path.insert(1, os.getcwd())
from src.domain.classes import book, client, rental
import datetime
import re
import unittest

def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__


class repository:
    def __init__(self,loading=''):
        self.books = []
        self.clients = []
        self.rents = []
        if loading=='':
            self.filebooks='src/repository/books.json'
            self.fileclients='src/repository/clients.json'
            self.filerents='src/repository/rental.json'
            self.load()
        else:
            self.filebooks='src/repository/bookstest.json'
            self.fileclients='src/repository/clientstest.json'
            self.filerents='src/repository/rentaltest.json'
        self.hist=[]
        self.redu=[]
        
    def prtBooks(self):
        for book in self.books:
            book.prt()
            
    def prtClients(self):
        for client in self.clients:
            client.prt()
        
    def prtRental(self):
        for rent in self.rents:
            rent.prt()
            
    def load(self):
        with open(self.filebooks) as f:
            self.books = json.load(f)
        for i in range(len(self.books)):
            bok = book(self.books[i])
            self.books[i]=bok
            
        with open(self.fileclients) as f:
            self.clients = json.load(f)
        for i in range(len(self.clients)):
            cli = client(self.clients[i])
            self.clients[i]=cli
            
        with open(self.filerents) as f:
            self.rents = json.load(f)
        for i in range(len(self.rents)):
            ren = rental(self.rents[i]['uuid'],book(self.rents[i]['book']),client(self.rents[i]['client']),self.rents[i]['datefrom'],self.rents[i]['dateto'])
            self.rents[i]=ren
            for index in range(len(self.books)):
                if self.books[index].uuid == ren.book.uuid:
                    self.books[index].rented=True
                    break
                
                
    def push(self):
        with open(self.filebooks, 'w') as f:
            json.dump(self.books, f,default = lambda x: x.__dict__)
        with open(self.fileclients, 'w') as f:
            json.dump(self.clients, f,default = lambda x: x.__dict__)
        with open(self.filerents, 'w') as f:
            json.dump(self.rents, f,default = lambda x: x.__dict__)
            
            
    def add(self,item):
        dictio={}
        dictio['cmd']='add'
        dictio['item']=item
        if item.__class__.__name__=='book':
            dictio['type']='book'
            self.books.append(item)
        else:
            dictio['type']='client'
            self.clients.append(item)
        self.push()
        self.hist.append(dictio)
        self.redu=[]
        return True
        
    def removeBook(self,query):
        dictio={}
        dictio['cmd']='remove'
        dictio['type']='book'
        dictio['item']=[]
        if query[0][0]=='#':
            query[0]=query[0][1:]
        if query[0][0]>='0' and query[0][0]<='9':
            atribute='uuid'
        else:
            atribute='name'
        ok=True
        query = " ".join(query)
        for book in self.books:
            if atribute=='uuid':
                if book.uuid == query:
                    dictio['item'].append(book)
                    self.books.remove(book)
                    self.push()
                    ok=False
            else:
                if book.name == query:
                    dictio['item'].append(book)
                    self.books.remove(book)
                    self.push()
                    ok=False
        if ok:
            raise ValueError("Book not found")
        if len(dictio['item'])>0:
            self.hist.append(dictio)
            self.redu=[]
        return True
                
    def removeClient(self,query):
        dictio={}
        dictio['cmd']='remove'
        dictio['type']='client'
        dictio['item']=[]
        if query[0][0]=='#':
            query[0]=query[0][1:]
        if query[0][0]>='0' and query[0][0]<='9':
            atribute='uuid'
        else:
            atribute='name'
        ok=True
        query = " ".join(query)
        for client in self.clients:
            if atribute=='uuid':
                if client.uuid == query:
                    dictio['item'].append(client)
                    self.clients.remove(client)
                    self.push()
                    ok=False
            else:
                if client.name == query:
                    dictio['item'].append(client)
                    self.clients.remove(client)
                    self.push()
                    ok=False
        if ok:
            raise ValueError("Client not found")
        if len(dictio['item'])>0:
            self.hist.append(dictio)
            self.redu=[]
        return True
                
    def updateBook(self,query):
        dictio={}
        dictio['cmd']='update'
        dictio['type']='book'
        dictio['itemOLD']=[]
        dictio['itemNEW']=[]
        if query[0][0]=='#':
            query[0]=query[0][1:]
        if query[0][0]>='0' and query[0][0]<='9':
            atribute='uuid'
        else:
            atribute='name'
        ok=True
        index=0
        for i in range(len(query)):
            if query[i]=='author' or query[i]=='name' or query[i]=='uuid':
                index=i
                break
        assert index >0, "ERROR: Invalid command"
        identifier=" ".join(query[:index])
        for book in self.books:
            if atribute=='uuid':
                if book.uuid == identifier:
                    dictio['itemOLD'].append(deepcopy(book))
                    if query[index]=='author':
                        book.author=" ".join(query[index+1:])
                    elif query[index]=='name':
                        book.name=" ".join(query[index+1:])
                    elif query[index]=='uuid':
                        book.uuid=" ".join(query[index+1:])
                    self.push()
                    ok=False
                    dictio['itemNEW'].append(deepcopy(book))
            else:
                if book.name == identifier:
                    dictio['itemOLD'].append(deepcopy(book))
                    if query[index]=='author':
                        book.author=" ".join(query[index+1:])
                    elif query[index]=='name':
                        book.name=" ".join(query[index+1:])
                    elif query[index]=='uuid':
                        book.uuid=" ".join(query[index+1:])
                    self.push()
                    ok=False
                    dictio['itemNEW'].append(deepcopy(book))
        if ok:
            raise ValueError("Book not found")
        if len(dictio['itemOLD'])>0:
            self.hist.append(dictio)
            self.redu=[]
        return True
                    

        
    def updateClient(self,query):
        dictio={}
        dictio['cmd']='update'
        dictio['type']='client'
        dictio['itemOLD']=[]
        dictio['itemNEW']=[]
        if query[0][0]=='#':
            query[0]=query[0][1:]
        if query[0][0]>='0' and query[0][0]<='9':
            atribute='uuid'
        else:
            atribute='name'
        ok=True
        index=0
        for i in range(len(query)):
            if query[i]=='name' or query[i]=='uuid':
                index=i
                break
        assert index >0, "ERROR: Invalid command"
        identifier=" ".join(query[:index])
        for client in self.clients:
            if atribute=='uuid':
                if client.uuid == identifier:
                    dictio['itemOLD'].append(deepcopy(client))
                    if query[index]=='name':
                        client.name=" ".join(query[index+1:])
                    elif query[index]=='uuid':
                        client.uuid=" ".join(query[index+1:])
                    self.push()
                    ok=False
                    dictio['itemNEW'].append(deepcopy(client))
            else:
                if client.name == identifier:
                    dictio['itemOLD'].append(deepcopy(client))
                    if query[index]=='name':
                        client.name=" ".join(query[index+1:])
                    elif query[index]=='uuid':
                        client.uuid=" ".join(query[index+1:])
                    self.push()
                    ok=False
                    dictio['itemNEW'].append(deepcopy(client))
        if ok:
            raise ValueError("Client not found")
        if len(dictio['itemOLD'])>0:
            self.hist.append(dictio)
            self.redu=[]
        return True
        
    def rent(self,query):
        #rent ceapa to pufi 
        dictio={}
        dictio['cmd']='rent'
        ok=False
        clientname=0
        bookname=0
        for i in reversed(range(len(query))):
            if query[i]=='to':
                ok=True
                clientname= " ".join(query[i+1:])
                if i==0:
                    raise ValueError("ERROR: Invalid command")
                bookname=" ".join(query[:i])
                break

        bookFound=0
        bookRented=0
            
        for book in self.books:
            if book.name == bookname or book.uuid==bookname:
                if book.rented:
                    bookRented=1
                    bookFound=1
                else:
                    bookRented=0
                    bookFound=1
                    ok=False
                    for client in self.clients:
                        if client.name == clientname or client.uuid==clientname:
                            self.rents.append(rental(str(randint(10000000000,19999999999))[1:],book,client,str(datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)),NULL))
                            book.rented=True
                            self.push()
                            dictio['item']=deepcopy(self.rents[-1])
                            break
                    if ok:
                        raise ValueError("Client not found")
                    break
        assert bookFound==1,"Book not found!"
        assert bookRented==0,"Every copy of that book was rented!"
        self.hist.append(dictio)
        self.redu=[]
        

    def retrn(self,query):
        #return ceapa from pufi
        #return Mat Lam Tam from Gianni Muscott
        ok=False
        dictio={}
        dictio['cmd']='return'
        clientname=0
        bookname=0
        for i in reversed(range(len(query))):
            if query[i]=='from':
                ok=True
                clientname= " ".join(query[i+1:])
                if i==0:
                    raise ValueError("ERROR: Invalid command")
                bookname=" ".join(query[:i])
                break
        bookFound=0
        correctClient=0
        for i in range(len(self.rents)):
            rent=self.rents[i]
            if rent.book.name == bookname or rent.book.uuid==bookname:
                bookFound=1
                if rent.client.name == clientname or rent.client.uuid==clientname:
                    correctClient=1
                    rent.dateto=str(datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
                    for book in self.books:
                        if book.uuid==rent.book.uuid:
                            book.rented=False
                            break
                    self.push()
                    dictio['item']=deepcopy(rent)
                    break

        assert bookFound==1,"Book not found!"
        assert correctClient==1,"Client did not rent that book!"
        self.hist.append(dictio)
        self.redu=[]

        
    def get(self,uuid):
        for book in self.books:
            if book['uuid'] == uuid:
                return book
            
    def get_list(self):
        return self.books
            
    def searchBookName(self,query):
        res=[]
        for book in self.books:
            if re.search(query,book.name, re.IGNORECASE):
                res.append(book)
        return res
                
    def searchBookAuthor(self,query):
        res=[]
        for book in self.books:
            if re.search(query,book.author, re.IGNORECASE):
                res.append(book)
        return res
                
    def searchBookUUID(self,query):
        res=[]
        for book in self.books:
            if re.search(query,book.uuid, re.IGNORECASE):
                res.append(book)
        return res

    def searchClientName(self,query):
        res=[]
        for client in self.clients:
            if re.search(query,client.name, re.IGNORECASE):
                res.append(client)
        return res
    
    def searchClientUUID(self,query):
        res=[]
        for client in self.clients:
            if re.search(query,client.uuid, re.IGNORECASE):
                res.append(client)
        return res
    
    def topBook(self,query):
        books ={}
        booklist =[]
        for rent in self.rents:
            if rent.book.name in books:
                books[rent.book.name]+=1
            else:
                books[rent.book.name]=1
                booklist.append(rent.book.name)
        booklist.sort(key=lambda x: books[x], reverse=True)
        if len(booklist)<=query:
            return (booklist,books)
        else:
            return booklist[:query]

            
    def topClient(self,query):
        clients={}
        clientlist=[]
        for re in self.rents:
            rent = copy(re)
            if rent.dateto==NULL:
                rent.dateto=datetime.datetime.now()
            else:
                rent.dateto=datetime.datetime(int(rent.dateto.split('-')[0]),int(rent.dateto.split('-')[1]),int(rent.dateto.split('-')[2]))
            rent.datefrom=datetime.datetime(int(rent.datefrom.split('-')[0]),int(rent.datefrom.split('-')[1]),int(rent.datefrom.split('-')[2]))
            if rent.client.name in clients:
                clients[rent.client.name]+=(rent.dateto-rent.datefrom).days
            else:
                clients[rent.client.name]=(rent.dateto-rent.datefrom).days
                clientlist.append(rent.client.name)
        clientlist.sort(key=lambda x: clients[x], reverse=True)
        if len(clientlist)<=query:
            return clientlist
        else:
            return clientlist[:query]
    
    def topAuthor(self,query):
        authors={}
        authorlist=[]
        for rent in self.rents:
            if rent.book.author in authors:
                authors[rent.book.author]+=1
            else:
                authors[rent.book.author]=1
                authorlist.append(rent.book.author)
        authorlist.sort(key=lambda x: authors[x], reverse=True)
        if len(authorlist)<=query:
            return authorlist
        else:
            return authorlist[:query]

    def undo(self):
        assert len(self.hist)>0, "ERROR! No more undos!"
        action=self.hist.pop()
        
        self.redu.append(action)
        if action['cmd']=='add':
            if action['type']=='book':
                for book in self.books:
                    if book==action['item']:
                        self.books.remove(book)
                        break
            else:
                for client in self.clients:
                    if client.uuid==action['uuid']:
                        self.clients.remove(client)
                        break
                    
        elif action['cmd']=='remove':
            if action['type']=='book':
                for item in action['item']:
                    self.books.append(item)
            else:
                for item in action['item']:
                    self.clients.append(item)
                    
        elif action['cmd']=='rent':
            for rent in self.rents:
                if rent.uuid==action['item'].uuid:
                    self.rents.remove(rent)
                    for book in self.books:
                        if book.uuid==rent.book.uuid:
                            book.rented=False
                            break
                    break
                
        elif action['cmd']=='return':
            for rent in self.rents:
                if rent.uuid==action['item'].uuid:
                    rent.dateto=NULL
                    for book in self.books:
                        if book.uuid==rent.book.uuid:
                            book.rented=True
                            break
                    break
                
        elif action['cmd']=='update':
            if action['type']=='book':
                for i in range(len(action['itemNEW'])):
                    for j in range(len(self.books)):
                        if self.books[j].uuid==action['itemNEW'][i].uuid:
                            self.books[j]=action['itemOLD'][i]
                            break
            else:
                for i in range(len(action['itemNEW'])):
                    for j in range(len(self.clients)):
                        if self.clients[j].uuid==action['itemNEW'][i].uuid:
                            self.clients[j]=action['itemOLD'][i]
                            break
        self.push()
                
    def redo(self):
        assert len(self.redu)>0, "ERROR! No more redos!"
        action=self.redu.pop()
        self.hist.append(action)
        if action['cmd']=='add':
            if action['type']=='book':
                self.books.append(action['item'])
            else:
                self.clients.append(action['item'])
                
        elif action['cmd']=='remove':
            if action['type']=='book':
                for item in action['item']:
                    self.books.remove(item)
            else:
                for item in action['item']:
                    self.clients.remove(item)
                    
        elif action['cmd']=='rent':
            self.rents.append(action['item'])
            for book in self.books:
                if book.uuid==action['item'].book.uuid:
                    book.rented=True
                    break
            
                
        elif action['cmd']=='return':
            for rent in self.rents:
                if rent.uuid==action['item'].uuid:
                    rent.dateto=action['item'].dateto
                    for book in self.books:
                        if book.uuid==rent.book.uuid:
                            book.rented=False
                            break
                    break
                
        elif action['cmd']=='update':
            if action['type']=='book':
                for i in range(len(action['itemNEW'])):
                    for j in range(len(self.books)):
                        if self.books[j].uuid==action['itemNEW'][i].uuid:
                            self.books[j]=action['itemNEW'][i]
                            break
            else:
                for i in range(len(action['itemNEW'])):
                    for j in range(len(self.clients)):
                        if self.clients[j].uuid==action['itemNEW'][i].uuid:
                            self.clients[j]=action['itemNEW'][i]
                            break
                        
        self.push()
        
                        

    
                            
    