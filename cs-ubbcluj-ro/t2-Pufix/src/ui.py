from services import service
class ui:
    def __init__(self):
        self.serv=service()
        print("\n"*200)
        
    def print_menu(self):
        print("1. List players")
        print("2. Display next round")
        print("3. Play next game")
        print("0. Exit")
        self.serv.verify()

    def print_players(self):
        print(self.serv.get_players())

    def read_command(self):
        cmd=input("Please enter the command: ")
        assert cmd.isnumeric()
        assert int(cmd)>=0 and int(cmd)<=3
        return int(cmd)

    def playNext(self):
        print("Winner is: "+self.serv.playRound())

    def display_rounds(self):
        if self.serv.display_rounds()[0]=='qual':
            print("The qualifier round: ")
        for rounds in self.serv.display_rounds():
            print(str(rounds[1])+" is playing with "+str(rounds[2]))