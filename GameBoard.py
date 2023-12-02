class GameBoard:
    def __init__(self, boardWidth, boardLength):
        self.board = [[0 for _ in range(boardLength)] for _ in range(boardWidth)]