class ui:
    def __init__(self,service):
        self.serv=service

    def cmd(self):
        try:
            print()
            cmd=self.getCmd()
            if cmd[0]=='exit' or cmd[0]=='ragequit' or cmd[0]=='quit':
                return False
            elif cmd[0]=='help' or cmd[0]=='helpmepls':
                self.printHelp()
            elif cmd[0]=='pull':
                self.serv.pull()
            elif cmd[0]=='push':
                self.serv.push()
            elif cmd[0]=='list':
                self.serv.list(cmd[1:])
            elif cmd[0]=='add':
                self.serv.add(cmd[1:])
            elif cmd[0]=='undo':
                self.serv.undo()
            elif cmd[0]=='delete' or cmd[0]=='remove':
                self.serv.remove(cmd[1:])
            elif cmd[0]=='update':
                self.serv.update(cmd[1:])
            elif cmd[0]=='rent':
                self.serv.rent(cmd[1:])
            elif cmd[0]=='return':
                self.serv.retrn(cmd[1:])
            elif cmd[0]=='search':
                self.search(cmd[1:])
            elif cmd[0]=='top':
                self.top(cmd[1:])
            elif cmd[0]=='redo':
                self.serv.redo()
                
        except (ValueError, AssertionError) as err:
            print(err)
        return True

    def top(self,query):
        results=self.serv.top(query)
        res=results[0]
        nbrs=results[1]
       
        index =1
        for r in res:
            print('#'+str(index)+': '+str(r)+ " with "+str(nbrs[r])+" rentals")
            index+=1
            
        
    
    def getCmd(self):
        cmd=input()
        command=cmd.split()
        cmdList=[
            "redo",
            "exit",
            "quit",
            "ragequit",
            "help",
            "pull",
            "push",
            "helpmepls",
            "list",
            "add",
            "undo",
            "delete",
            "remove",
            "update",
            "rent",
            "return",
            "search",
            "top",
            ]
        ok=0
        assert len(command)!=0, ""
        if command[0] in cmdList:
            ok=1
        assert ok == 1, "ERROR: Invalid command!"
        print()
        return command

    def search(self,query):
        results=self.serv.search(query)
        print("Here are the results: ")
        if len(results)==0:
            print("    No results found!")
        else:
            for res in results:
                res.prt()
        

    def printHelp(self):
        print("    add <client/book> - adds a new element")
        print("    remove <client/book> - removes an element")
        print("    update <client/book> <name/uuid> <name/author/uuid> <query> - updates an element")
        print("    list <clients/books/rents> - lists all elements")
        print("    rent <book> to <client> - rents a book to a client")
        print("    return <book> from <client> - returns a book from a client")
        print("    search <book/client> <name/author/uuid> <query> - searches for a book or a client")
        print("    top <book/author/client> <nr_of_results> - prints the statistic")
        print("    undo - undoes the last operation")
        print("    redo - redoes the last operation")
        print("    pull - pulls the data from the server")
        print("    push - pushes the data to the server")
        print("    help - prints this help")
        print("    exit - exits the program")
        print("    quit - exits the program")
        print()
        
        