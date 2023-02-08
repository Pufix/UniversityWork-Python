import serv
import texttable
import pickle
class ui:
    def __init__(self):
        self.serv=serv.serv()
        x=input("Do you want to load a game? (y/n)")
        if x=='y':
            f=open("save.txt","rb")
            self.serv=pickle.load(f)
            f.close()

    def printing(self):
        table=self.serv.get_table()
        t=texttable.Texttable()
        t.add_rows(table)
        print(t.draw())

    def get_move(self):
        try:
            print("If you desire to save the game, simply type -1 into any text box")
            x=int(input("x="))-1
            if x==-2:
                self.save_game()
                return 0
            y=int(input("y="))-1
            if y==-2:
                self.save_game()
                return 0
            v=int(input("v="))
            if v==0:
                v='O'
            elif v==1:
                v='X'
            elif v==-1:
                self.save_game()
                return 0
            return self.serv.move(x,y,v)
        except:
            print("Invalid input!")
            return 1
        
    def save_game(self):
        f=open("save.txt","wb")
        pickle.dump(self.serv,f)
        f.close()