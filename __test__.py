import unittest
from app import Connect4Game
class TestConnect4Game(unittest.TestCase):
    def setUp(self):
        # Initialize the Connect4Game instance for each test
        self.connect4 = Connect4Game()

    def test_isColFull(self):
        # Test isColFull for an empty column
        self.assertFalse(self.connect4.isColFull(0))

        # Test isColFull after inserting a move
        self.connect4.insertMove(0, self.connect4.player1sym)
        self.assertFalse(self.connect4.isColFull(0))

        # Fill the column
        for i in range(self.connect4.length):
            self.connect4.insertMove(0, self.connect4.player1sym)
        self.assertTrue(self.connect4.isColFull(0))

    def test_isGameFull(self):
        # Test isGameFull for an empty game
        self.assertFalse(self.connect4.isGameFull())

        # Fill the entire game board
        for i in range(self.connect4.width):
            for j in range(self.connect4.length):
                self.connect4.insertMove(i, self.connect4.player1sym)
        self.assertTrue(self.connect4.isGameFull())

    def test_increaseScore(self):
        # Test increaseScore for player 1
        self.connect4.increaseScore(self.connect4.player1sym)
        self.assertEqual(self.connect4.player1Score, 1)

        # Test increaseScore for player 2
        self.connect4.increaseScore(self.connect4.player2sym)
        self.assertEqual(self.connect4.player2Score, 1)

    def test_possibleMoves(self):
        # Test possibleMoves for an empty game
        moves = self.connect4.possibleMoves(self.connect4.player1sym, self.connect4.game)
        self.assertEqual(len(moves), self.connect4.width)

        # Test possibleMoves after filling a column
        for i in range(self.connect4.length):
            self.connect4.insertMove(0, self.connect4.player1sym)
        moves = self.connect4.possibleMoves(self.connect4.player1sym, self.connect4.game)
        self.assertEqual(len(moves), self.connect4.width - 1)
        
    def test_insertMove(self):
        # Test insertMove for inserting a move in an empty column
        self.connect4.insertMove(0, self.connect4.player1sym)
        self.assertEqual(self.connect4.game[0][5], self.connect4.player1sym)

        # Test insertMove for inserting a move in a non-empty column
        self.connect4.insertMove(0, self.connect4.player2sym)
        self.assertEqual(self.connect4.game[0][4], self.connect4.player2sym)

    def test_getHiestEmptyCell(self):
        # Test getHighestEmptyCell for an empty column
        result = self.connect4.getHiestEmptyCell(0, self.connect4.game)
        self.assertEqual(result, self.connect4.length - 1)

        # Test getHighestEmptyCell after inserting a move
        self.connect4.insertMove(0, self.connect4.player1sym)
        result = self.connect4.getHiestEmptyCell(0, self.connect4.game)
        self.assertEqual(result, self.connect4.length - 2)
        
    def test_numOf4Connected(self):
        # Test numOf4Connected for horizontal connections
        self.connect4.insertMove(1, self.connect4.player1sym)
        self.connect4.insertMove(1, self.connect4.player1sym)
        self.connect4.insertMove(1, self.connect4.player1sym)
        self.assertEqual(self.connect4.numOf4Connected(self.connect4.player1sym), 0)

        # Test numOf4Connected for vertical connections
        self.connect4.insertMove(1, self.connect4.player1sym)
        self.assertEqual(self.connect4.numOf4Connected(self.connect4.player1sym), 1)

        # Add more test cases for diagonal and other connections
        
        def test_result(self):
                # Test result for player 1 winning
                for i in range(4):
                    self.connect4.insertMove(i, self.connect4.player1sym)
                result = self.connect4.result()
                self.assertEqual(result, "player 1")

                # Test result for player 2 winning
                self.connect4 = Connect4Game()  # Reset the game
                for i in range(4):
                    self.connect4.insertMove(i, self.connect4.player2sym)
                result = self.connect4.result()
                self.assertEqual(result, "player 2")

            # Add more test cases for a tie or other scenarios
if __name__ == '__main__':
    unittest.main()
