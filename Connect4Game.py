from Player import Player
from ComputerPlayer import ComputerPlayer
from GameBoard import GameBoard
class Connect4Game:
    def __init__(self, player1Sym, player2Sym, boardWidth, boardLength):
        self.player1 = Player(player1Sym, player2Sym)
        self.player2 = ComputerPlayer(player2Sym, player1Sym) 
        self.gameBoard = GameBoard(boardWidth, boardLength)
