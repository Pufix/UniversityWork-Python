import repo
class serv:
    def __init__(self):
        self.repo=repo.repo()
        
    def move(self,x,y,v):
        valid = self.repo.get_valid_moves()
        if [x,y] in valid:
            self.repo.move(x,y,v)
            if self.repo.checkwinok():
                print("Order wins!")
                return 0
            if self.repo.get_valid_moves()==[]:
                print("Chaos wins!")
                return 0
            self.repo.ai_move()
            if self.repo.checkwinok():
                print("Order wins!")
                return 0
            if self.repo.get_valid_moves()==[]:
                print("Chaos wins!")
                return 0
            return 1
        
    def get_table(self):
        return self.repo.matrix