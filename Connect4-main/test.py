from Connect4Game import Connect4Game
from gameLogic import insertMove
import time


game = Connect4Game(1 ,-1 ,7, 6)
game.gameBoard.board = [[0, 0, 0,  0,  1, 1], 
                        [0, 0, 0,  0,  1, -1], 
                        [0, 0, 0,  0, 1,  -1], 
                        [0, 0, 0, 0,  1,  -1], 
                        [0, 0, 0, 1, -1,   1], 
                        [0, 0, 0, 1, 1,   -1], 
                        [0, 0, 0, -1, -1,  -1]
                        ]
""" print(game.gameBoard.board)
print(game.player1.sym)
print(game.player2.sym)

move1 = game.player2.getMove(game.player2.sym, game.gameBoard.board, 0) 
print("move1"+  str(move1))
print("col: " + str(move1[1]))
insertMove(move1[1], game.player2.sym, game.gameBoard.board)
print(game.gameBoard.board) """


print(game.gameBoard)
print(game.player1.sym)
print(game.player2.sym)

start= time.time()
move1= game.player2.getMove(game.player2.sym, game.gameBoard.board, 0,True) 
end= time.time()

print("move1"+  str(move1))
print("nodes expanded :" + str(move1[2]))
print("col: " + str(move1[1]))
print("time taken: " + str(end-start))
insertMove(move1[1], game.player2.sym, game.gameBoard.board)
print(game.gameBoard.board)


game.gameBoard.board = [[0, 0, 0,  0,  1, 1], 
                        [0, 0, 0,  0,  1, -1], 
                        [0, 0, 0,  0, 1,  -1], 
                        [0, 0, 0, 0,  1,  -1], 
                        [0, 0, 0, 1, -1,   1], 
                        [0, 0, 0, 1, 1,   -1], 
                        [0, 0, 0, -1, -1,  -1]
                        ]


print(game.gameBoard.board)
print(game.player1.sym)
print(game.player2.sym)

start= time.time()
move1 = game.player2.exp__getMove(game.player2.sym, game.gameBoard.board, 0) 
end= time.time()

print("move1"+  str(move1))
print("col: " + str(move1[1]))
print("time taken: " + str(end-start))

insertMove(move1[1], game.player2.sym, game.gameBoard.board)
print(game.gameBoard.board)