from Connect4Game import Connect4Game
from gameLogic import insertMove
game = Connect4Game(1 ,-1 ,7, 6)
game.gameBoard.board = 
print(game.gameBoard.board)
print(game.player1.sym)
print(game.player2.sym)

move1 = game.player2.getMove(game.player2.sym, game.gameBoard.board, 0) 
print("col: " + str(move1[1]))
insertMove(move1[1], game.player2.sym, game.gameBoard.board)
print(game.gameBoard.board)

