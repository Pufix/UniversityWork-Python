import random
class repo:
    def __init__(self):
        self.matrix=[[' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ']]
        
    def move(self,x,y,v):
        self.matrix[x][y]=v

    def get_valid_moves(self):
        results=[]
        for i in range (6):
            for j in range (6):
                if self.matrix[i][j]==' ':
                    results.append([i,j])
        return results
                
    def check_win(self,i,j):
        if self.check_line(i,j)!=0:
            return self.check_line(i,j)
        if self.check_col(i,j)!=0:
            return self.check_col(i,j)
        if self.check_diag(i,j)!=0:
            return self.check_diag(i,j)
        if self.check_diag2(i,j)!=0:
            return self.check_diag2(i,j)
        return 0
    
    def ai_move(self):
        #the computer tries to parry the win, if it doesnt have to parry it makes a random move
        parry=self.parry_win()
        if parry==0:
            choice = random.choice(['O','X'])
            moves=self.get_valid_moves()
            if len(moves)==0:
                return 0
            move=random.choice(moves)
            self.move(move[0],move[1],choice)
            return choice
        return parry

    def parry_win(self):
        for i in range (6):
            for j in range (6):
                if self.check_win(i,j)=='O':
                    self.move(i,j,'X')
                    return 'X'
                elif self.check_win(i,j)=='X':
                    self.move(i,j,'O')
                    return 'O'
        return 0

    def check_diag(self,i,j):
        if self.matrix[i][j]!=' ':
            return 0
        try:
            if self.matrix[i+1][j+1]==self.matrix[i+2][j+2] and self.matrix[i+2][j+2]==self.matrix[i+3][j+3] and self.matrix[i+3][j+3]==self.matrix[i+4][j+4] and self.matrix[i+1][j+1]!=' ':
                return self.matrix[i+1][j+1]
        except:
            pass
        try:
            if self.matrix[i-1][j-1]==self.matrix[i+1][j+1] and self.matrix[i+1][j+1]==self.matrix[i+2][j+2] and self.matrix[i+2][j+2]==self.matrix[i+3][j+3] and self.matrix[i-1][j-1]!=' ':
                return self.matrix[i-1][j-1]
        except:
            pass
        try:
            if self.matrix[i-2][j-2]==self.matrix[i-1][j-1] and self.matrix[i-1][j-1]==self.matrix[i+1][j+1] and self.matrix[i+1][j+1]==self.matrix[i+2][j+2] and self.matrix[i-2][j-2]!=' ':
                return self.matrix[i-2][j-2]
        except:
            pass
        try:
            if self.matrix[i-3][j-3]==self.matrix[i-2][j-2] and self.matrix[i-2][j-2]==self.matrix[i-1][j-1] and self.matrix[i-1][j-1]==self.matrix[i+1][j+1] and self.matrix[i-3][j-3]!=' ':
                return self.matrix[i-3][j-3]
        except:
            pass
        try:
            if self.matrix[i-4][j-4]==self.matrix[i-3][j-3] and self.matrix[i-3][j-3]==self.matrix[i-2][j-2] and self.matrix[i-2][j-2]==self.matrix[i-1][j-1] and self.matrix[i-4][j-4]!=' ':
                return self.matrix[i-4][j-4]
        except:
            pass
        return 0
    
    def check_diag2(self,i,j):
        if self.matrix[i][j]!=' ':
            return 0
        try:
            if self.matrix[i+1][j-1]==self.matrix[i+2][j-2] and self.matrix[i+2][j-2]==self.matrix[i+3][j-3] and self.matrix[i+3][j-3]==self.matrix[i+4][j-4] and self.matrix[i+1][j-1]!=' ':
                return self.matrix[i+1][j-1]
        except:
            pass
        try:
            if self.matrix[i-1][j+1]==self.matrix[i+1][j-1] and self.matrix[i+1][j-1]==self.matrix[i+2][j-2] and self.matrix[i+2][j-2]==self.matrix[i+3][j-3] and self.matrix[i-1][j+1]!=' ':
                return self.matrix[i-1][j+1]
        except:
            pass
        try:
            if self.matrix[i-2][j+2]==self.matrix[i-1][j+1] and self.matrix[i-1][j+1]==self.matrix[i+1][j-1] and self.matrix[i+1][j-1]==self.matrix[i+2][j-2] and self.matrix[i-2][j+2]!=' ':
                return self.matrix[i-2][j+2]
        except:
            pass
        try:
            if self.matrix[i-3][j+3]==self.matrix[i-2][j+2] and self.matrix[i-2][j+2]==self.matrix[i-1][j+1] and self.matrix[i-1][j+1]==self.matrix[i+1][j-1] and self.matrix[i-3][j+3]!=' ':
                return self.matrix[i-3][j+3]
        except:
            pass
        try:
            if self.matrix[i-4][j+4]==self.matrix[i-3][j+3] and self.matrix[i-3][j+3]==self.matrix[i-2][j+2] and self.matrix[i-2][j+2]==self.matrix[i-1][j+1] and self.matrix[i-4][j+4]!=' ':
                return self.matrix[i-4][j+4]
        except:
            pass
        return 0

    def check_line(self,i,j):
        if self.matrix[i][j]!=' ':
            return 0
        try:
            if self.matrix[i+1][j]==self.matrix[i+2][i] and self.matrix[i+2][j]==self.matrix[i+3][j] and self.matrix[i+3][j]==self.matrix[i+4][j] and self.matrix[i+1][j]!=' ':
                return self.matrix[i+1][j]
        except:
            pass
        try:
            if self.matrix[i-1][j]==self.matrix[i+1][j] and self.matrix[i+1][j]==self.matrix[i+2][j] and self.matrix[i+2][j]==self.matrix[i+3][j] and self.matrix[i-1][j]!=' ':
                return self.matrix[i-1][j]
        except:
            pass
        try:
            if self.matrix[i-2][j]==self.matrix[i-1][j] and self.matrix[i-1][j]==self.matrix[i+1][j] and self.matrix[i+1][j]==self.matrix[i+2][j] and self.matrix[i-2][j]!=' ':
                return self.matrix[i-2][j]
        except:
            pass
        try:
            if self.matrix[i-3][j]==self.matrix[i-2][j] and self.matrix[i-2][j]==self.matrix[i-1][j] and self.matrix[i-1][j]==self.matrix[i+1][j] and self.matrix[i-3][j]!=' ':
                return self.matrix[i-3][j]
        except:
            pass
        try:
            if self.matrix[i-4][j]==self.matrix[i-3][j] and self.matrix[i-3][j]==self.matrix[i-2][j] and self.matrix[i-2][j]==self.matrix[i-1][j] and self.matrix[i-4][j]!=' ':
                return self.matrix[i-4][j]
        except:
            pass
        return 0

    def check_col(self,i,j):
        if self.matrix[i][j]!=' ':
            return 0
        try:
            if self.matrix[i][j+1]==self.matrix[i][j+2] and self.matrix[i][j+2]==self.matrix[i][j+3] and self.matrix[i][j+3]==self.matrix[i][j+4] and self.matrix[i][j+1]!=' ':
                return self.matrix[i][j+1]
        except:
            pass
        try:
            if self.matrix[i][j-1]==self.matrix[i][j+1] and self.matrix[i][j+1]==self.matrix[i][j+2] and self.matrix[i][j+2]==self.matrix[i][j+3] and self.matrix[i][j-1]!=' ':
                return self.matrix[i][j-1]
        except:
            pass
        try:
            if self.matrix[i][j-2]==self.matrix[i][j-1] and self.matrix[i][j-1]==self.matrix[i][j+1] and self.matrix[i][j+1]==self.matrix[i][j+2] and self.matrix[i][j-2]!=' ':
                return self.matrix[i][j-2]
        except:
            pass
        try:
            if self.matrix[i][j-3]==self.matrix[i][j-2] and self.matrix[i][j-2]==self.matrix[i][j-1] and self.matrix[i][j-1]==self.matrix[i][j+1] and self.matrix[i][j-3]!=' ':
                return self.matrix[i][j-3]
        except:
            pass
        try:
            if self.matrix[i][j-4]==self.matrix[i][j-3] and self.matrix[i][j-3]==self.matrix[i][j-2] and self.matrix[i][j-2]==self.matrix[i][j-1] and self.matrix[i][j-4]!=' ':
                return self.matrix[i][j-4]
        except:
            pass
        return 0
           
    def get_table(self):
        return self.matrix
    
    def checkwinok(self):
        for i in range(0,6):
            for j in range(0,2):
                if self.matrix[i][j]!=' ' and self.matrix[i][j]==self.matrix[i][j+1] and self.matrix[i][j+1]==self.matrix[i][j+2] and self.matrix[i][j+2]==self.matrix[i][j+3] and self.matrix[i][j+3]==self.matrix[i][j+4]:
                    return self.matrix[i][j]
        for i in range(0,2):
            for j in range(0,6):
                if self.matrix[i][j]!=' ' and self.matrix[i][j]==self.matrix[i+1][j] and self.matrix[i+1][j]==self.matrix[i+2][j] and self.matrix[i+2][j]==self.matrix[i+3][j] and self.matrix[i+3][j]==self.matrix[i+4][j]:
                    return self.matrix[i][j]
        for i in range(0,2):
            for j in range(0,2):
                if self.matrix[i][j]!=' ' and self.matrix[i][j]==self.matrix[i+1][j+1] and self.matrix[i+1][j+1]==self.matrix[i+2][j+2] and self.matrix[i+2][j+2]==self.matrix[i+3][j+3] and self.matrix[i+3][j+3]==self.matrix[i+4][j+4]:
                    return self.matrix[i][j]
        for i in range(0,2):
            for j in range(4,6):
                if self.matrix[i][j]!=' ' and self.matrix[i][j]==self.matrix[i+1][j-1] and self.matrix[i+1][j-1]==self.matrix[i+2][j-2] and self.matrix[i+2][j-2]==self.matrix[i+3][j-3] and self.matrix[i+3][j-3]==self.matrix[i+4][j-4]:
                    return self.matrix[i][j]
        return 0

def test():
    rep=repo()
    rep.matrix=[['O','O','O','O',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
    rep.ai_move()
        
    assert rep.matrix[0][4]=='X'
        
    rep.matrix=[['O','O',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
    oldmatrix=[['O','O',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
    rep.ai_move()
    assert rep.matrix!=oldmatrix
    
        
if __name__=="__main__":
    test()
        