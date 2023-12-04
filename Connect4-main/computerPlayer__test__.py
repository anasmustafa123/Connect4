import unittest
from ComputerPlayer import ComputerPlayer 
class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        # Initialize the Connect4Game instance for each test
        self.computerPlayer = ComputerPlayer()
        
    def easy__test_getMove(self):
        board = [[0, 0, 0,  0,  1, 1], 
                [0, 0, 0,  0,  1, -1], 
                [0, 0, 0,  0, 1,  -1], 
                [0, 0, 0, 0,  1,  -1], 
                [0, 0, 0, 1, -1,   1], 
                [0, 0, 0, 1, 1,   -1], 
                [0, 0, 0, -1, -1, -1]
                ]
        result = self.computerPlayer.getMove(self.computerPlayer.sym, board, 0)
        print("col is : "+ str(result[1]))
        self.assertEqual(result[1], 6)
        
    def hard__test_getMove(self):
        board = [[0, 0, 0,  0,  1, 1], 
                [0, 0, 0,  0,  1, -1], 
                [0, 0, 0,  0, 1,  -1], 
                [0, 0, 0, 0,  1,  -1], 
                [0, 0, 0, 1, -1,   1], 
                [0, 0, 0, 1, 1,   -1], 
                [0, 0, 0, -1, -1, -1]
                ]
        result = self.computerPlayer.getMove(self.computerPlayer.sym, board, 0)
        print("col is : "+ str(result[1]))
        self.assertEqual(result[1], 6)


if __name__ == '__main__':
    unittest.main()
