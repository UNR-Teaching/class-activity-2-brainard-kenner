import unittest
from tictactoe import Board

class TicTacToeTester(unittest.TestCase):
    
    def test_add_o(self):
        board = Board()
        self.assertTrue(board.mark_square(0, 0, 'O'), "Not able to add an O to an empty board")
        self.assertEqual(board.board[0][0], 'O', "O was not sucessfully added to the empty board")


if __name__ == "__main__":
    unittest.main()