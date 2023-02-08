import sys
import os
sys.path.insert(1, os.getcwd())
import src.gameLogic.mainLogic


def initialize():
    game = src.gameLogic.mainLogic.game()
    game.board.aiMove()
    running = True
    while running:
        print('\n'*200)
        print(game.board)
        try:
            col = int(input('Enter column: '))-1
            assert col>=0
            assert col<=6
            game.board.addPiece(col, 'Y')
            if game.board.checkWin():
                print('\n'*200)
                print(game.board)
                print('Yellow wins!')
                running = False
                break
            game.board.aiMove()
            if game.board.checkWin():
                print('\n'*200)
                print(game.board)
                print('Red wins!')
                running = False
        except:
            pass
            
            