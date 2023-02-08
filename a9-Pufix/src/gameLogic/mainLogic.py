from copy import deepcopy
import math
import random
import sys
import os
import unittest
sys.path.insert(1,os.getcwd())
class game:
    def __init__(self):
        self.board = board()

    def setBoard(self):
        self.board = board()

def blueSquare():
    return '\u001b[34m■\u001b[0m'

def redSquare():
    return '\u001b[31m■\u001b[0m'

def yellowSquare():
    return '\u001b[33m■\u001b[0m'

def whiteSquare():
    return '■'

class board:
    def __init__(self):
        self.board =[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        
    def __str__(self):
        bord=blueSquare()*15+'\n'
        for line in range(6):
            bord+=blueSquare()
            for col in range(7):
                if self.board[line][col]==0:
                    bord+=whiteSquare()
                elif self.board[line][col]=='R':
                    bord+=redSquare()
                elif self.board[line][col]=='Y':
                    bord+=yellowSquare()
                bord+=blueSquare()
            bord+='\n'
        bord+=blueSquare()*15+'\n'
        return bord
            
    def addPiece(self, col, player):
        for line in reversed(range(6)):
            if self.board[line][col]==0:
                self.board[line][col]=player
                return

    def checkWin(self):
        for line in range(6):
            for col in range(7):
                if self.board[line][col]!=0:
                    if self.checkLine(line, col):
                        return True
        return False
    
    def checkLine(self, line, col):
        if self.board[line][col]==0:
            return False
        if self.checkHorizontal(line, col):
            return True
        if self.checkVertical(line, col):
            return True
        if self.checkDiagonal(line, col):
            return True
        if self.checkDiagonal2(line, col):
            return True
        return False

    def checkHorizontal(self, line, col):
        if col>3:
            return False
        for i in range(4):
            if self.board[line][col+i]!=self.board[line][col]:
                return False
        return True
    
    def checkVertical(self, line, col):
        if line>2:
            return False
        for i in range(4):
            if self.board[line+i][col]!=self.board[line][col]:
                return False
        return True
    
    def checkDiagonal(self, line, col):
        if line>2 or col>3:
            return False
        for i in range(4):
            if self.board[line+i][col+i]!=self.board[line][col]:
                return False
        return True
    
    def checkDiagonal2(self, line, col):
        if line>2 or col<3:
            return False
        for i in range(4):
            if self.board[line+i][col-i]!=self.board[line][col]:
                return False
        return True
    
    def checkDraw(self):
        for line in range(6):
            for col in range(7):
                if self.board[line][col]==0:
                    return False
        return True
    

    
    def getBoard(self):
        return self.board
    
    def aiMove(self):
        self.addPiece(self.minimax('R',3)[0],'R')

    def minimax(self,player,depth):
        validLocations=self.getValidLocations()
        isTerminal=self.isTerminalNode()
        if depth==0 or isTerminal:
            if isTerminal:
                if self.checkWin():
                    if player=='R':
                        return (None,100000000000000)
                    else:
                        return (None,-10000000000000)
                else:
                    return (None,0)
            else:
                return None,self.scorePosition(player)
        if player=='R':
            value=-math.inf
            column=random.choice(validLocations)
            for col in validLocations:
                b_copy=deepcopy(self.board)
                self.addPiece(col,player)
                newScore=self.minimax('Y',depth-1)[1]
                self.board=b_copy
                if newScore>value:
                    value=newScore
                    column=col
            return column,value
        else:
            value=math.inf
            column=random.choice(validLocations)
            for col in validLocations:
                b_copy=deepcopy(self.board)
                self.addPiece(col,player)
                newScore=self.minimax('R',depth-1)[1]
                self.board=b_copy
                if newScore<value:
                    value=newScore
                    column=col
            return column,value
    
    def scorePosition(self, player):
        score=0
        oponent='Y'
        if player=='Y':
            oponent='R'
        for row in range(3,5):
            for col in range(7):
                if self.board[row][col]==player and self.board[row-1][col]==player and self.board[row-2][col]==player and self.board[row-3][col]==player:
                    score+=100
                if self.board[row][col]==oponent and self.board[row-1][col]==oponent and self.board[row-2][col]==oponent and self.board[row-3][col]==oponent:
                    score-=1000
                if self.board[row][col]==player and self.board[row-1][col]==player and self.board[row-2][col]==player:
                    score+=10
                if self.board[row][col]==oponent and self.board[row-1][col]==oponent and self.board[row-2][col]==oponent:
                    score-=100
                if self.board[row][col]==player and self.board[row-1][col]==player:
                    score+=1
                if self.board[row][col]==oponent and self.board[row-1][col]==oponent:
                    score-=10

        for row in range(6):
            for col in range(4):
                if self.board[row][col]==player and self.board[row][col+1]==player and self.board[row][col+2]==player and self.board[row][col+3]==player:
                    score+=100
                if self.board[row][col]==oponent and self.board[row][col+1]==oponent and self.board[row][col+2]==oponent and self.board[row][col+3]==oponent:
                    score-=1000
                if self.board[row][col]==player and self.board[row][col+1]==player and self.board[row][col+2]==player:
                    score+=10
                if self.board[row][col]==oponent and self.board[row][col+1]==oponent and self.board[row][col+2]==oponent:
                    score-=100
                if self.board[row][col]==player and self.board[row][col+1]==player:
                    score+=1
                if self.board[row][col]==oponent and self.board[row][col+1]==oponent:
                    score-=10

        for row in range(3,5):
            for col in range(4):
                if self.board[row][col]==player and self.board[row-1][col+1]==player and self.board[row-2][col+2]==player and self.board[row-3][col+3]==player:
                    score+=100
                if self.board[row][col]==oponent and self.board[row-1][col+1]==oponent and self.board[row-2][col+2]==oponent and self.board[row-3][col+3]==oponent:
                    score-=1000
                if self.board[row][col]==player and self.board[row-1][col+1]==player and self.board[row-2][col+2]==player:
                    score+=10
                if self.board[row][col]==oponent and self.board[row-1][col+1]==oponent and self.board[row-2][col+2]==oponent:
                    score-=100
                if self.board[row][col]==player and self.board[row-1][col+1]==player:
                    score+=1
                if self.board[row][col]==oponent and self.board[row-1][col+1]==oponent:
                    score-=10
                    
        for row in range(2):
            for col in range(4):
                if self.board[row][col]==player and self.board[row+1][col+1]==player and self.board[row+2][col+2]==player and self.board[row+3][col+3]==player:
                    score+=100
                if self.board[row][col]==oponent and self.board[row+1][col+1]==oponent and self.board[row+2][col+2]==oponent and self.board[row+3][col+3]==oponent:
                    score-=1000
                if self.board[row][col]==player and self.board[row+1][col+1]==player and self.board[row+2][col+2]==player:
                    score+=10
                if self.board[row][col]==oponent and self.board[row+1][col+1]==oponent and self.board[row+2][col+2]==oponent:
                    score-=100
                if self.board[row][col]==player and self.board[row+1][col+1]==player:
                    score+=1
                if self.board[row][col]==oponent and self.board[row+1][col+1]==oponent:
                    score-=10
                    
        return score

    def getValidLocations(self):
        validLocations=[]
        for col in range(7):
            if self.board[0][col]==0:
                validLocations.append(col)
        return validLocations

    def isTerminalNode(self):
        return self.checkWin() or self.checkDraw()
    
    def getOpenRow(self,col):
        for row in range(6):
            if self.board[row][col]==0:
                return row
            
            
#make me a test class to test the board class
class TestBoard(unittest.TestCase):
    def test_addPiece(self):
        b=board()
        b.addPiece(0,'R')
        self.assertEqual(b.board[5][0],'R')
        b.addPiece(0,'Y')
        self.assertEqual(b.board[4][0],'Y')
        b.addPiece(0,'R')
        self.assertEqual(b.board[3][0],'R')
        b.addPiece(0,'Y')
        self.assertEqual(b.board[2][0],'Y')
        b.addPiece(0,'R')
        self.assertEqual(b.board[1][0],'R')
        b.addPiece(0,'Y')
        self.assertEqual(b.board[0][0],'Y')
        b.addPiece(0,'R')
        self.assertEqual(b.board[0][0],'Y')
        b.addPiece(1,'R')
        self.assertEqual(b.board[5][1],'R')
        b.addPiece(1,'Y')
        self.assertEqual(b.board[4][1],'Y')
        b.addPiece(1,'R')
        self.assertEqual(b.board[3][1],'R')
        b.addPiece(1,'Y')
        self.assertEqual(b.board[2][1],'Y')
        b.addPiece(1,'R')
        self.assertEqual(b.board[1][1],'R')
        b.addPiece(1,'Y')
        self.assertEqual(b.board[0][1],'Y')
        b.addPiece(1,'R')
        self.assertEqual(b.board[0][1],'Y')
        b.addPiece(2,'R')
        self.assertEqual(b.board[5][2],'R')
        b.addPiece(2,'Y')
        self.assertEqual(b.board[4][2],'Y')
        b.addPiece(2,'R')
        self.assertEqual(b.board[3][2],'R')
        b.addPiece(2,'Y')
        self.assertEqual(b.board[2][2],'Y')
        b.addPiece(2,'R')
        self.assertEqual(b.board[1][2],'R')
        b.addPiece(2,'Y')
        self.assertEqual(b.board[0][2],'Y')
        b.addPiece(2,'R')
        self.assertEqual(b.board[0][2],'Y')
        b.addPiece(3,'R')
        self.assertEqual(b.board[5][3],'R')
        b.addPiece(3,'Y')
        self.assertEqual(b.board[4][3],'Y')
        b.addPiece(3,'R')
        self.assertEqual(b.board[3][3],'R')

    def test_checkWin(self):
        b=board()
        b.addPiece(0,'R')
        b.addPiece(1,'R')
        b.addPiece(2,'R')
        b.addPiece(3,'R')
        self.assertEqual(b.checkWin(),True)
        b=board()
        b.addPiece(0,'Y')
        b.addPiece(1,'Y')
        b.addPiece(2,'Y')
        b.addPiece(3,'Y')
        self.assertEqual(b.checkWin(),True)
        b=board()
        b.addPiece(0,'R')
        self.assertEqual(b.checkWin(),False)
        b.addPiece(0,'R')
        b.addPiece(0,'R')
        b.addPiece(0,'R')
        self.assertEqual(b.checkWin(),True)

        b=board()
        b.addPiece(0,'R')
        b.addPiece(0,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'R')
        b.addPiece(1,'R')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(2,'Y')
        b.addPiece(1,'Y')
        b.addPiece(0,'Y')
        self.assertEqual(b.checkWin(),True)
        
        b=board()
        b.addPiece(6,'R')
        b.addPiece(6,'R')
        b.addPiece(6,'R')
        b.addPiece(5,'R')
        b.addPiece(5,'R')
        b.addPiece(4,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'Y')
        b.addPiece(5,'Y')
        b.addPiece(6,'Y')
        self.assertEqual(b.checkWin(),True)
        
    def test_checkDraw(self):
        b=board()
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        self.assertEqual(b.checkDraw(),True)

    def test_getValidLocations(self):
        b=board()
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        b.addPiece(3,'Y')
        b.addPiece(4,'R')
        b.addPiece(5,'Y')
        b.addPiece(6,'R')
        b.addPiece(0,'R')
        b.addPiece(1,'Y')
        b.addPiece(2,'R')
        
        self.assertEqual(b.getValidLocations(),[0,1,2,3,4,5,6])
        
if __name__ == '__main__':
    unittest.main()