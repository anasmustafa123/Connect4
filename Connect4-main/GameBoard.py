class GameBoard:
    def __init__(self, boardWidth, boardLength):
        self.board = [[0 for _ in range(boardLength)] for _ in range(boardWidth)]
        
    def __str__(self):
        # Convert the 2D array to a grid format
        grid_str = "\n".join([" ".join(map(str, row)) for row in self.board])
        return grid_str