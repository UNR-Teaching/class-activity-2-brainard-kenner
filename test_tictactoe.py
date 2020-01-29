import unittest
from tictactoe import Board

class TicTacToeTester(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TicTacToeTester, self).__init__(*args, **kwargs)
        self.board = None

    def setUp(self):
        self.board = Board()

    def test_mark_square_normal_use_X(self):
        self.assertTrue(self.board.mark_square(1, 2, 'X'))
        self.assertEqual(self.board.board[1][2], 'X')
    
    def test_mark_square_normal_use_O(self):
        self.assertTrue(self.board.mark_square(1, 2, 'O'))
        self.assertEqual(self.board.board[1][2], 'O')

    def test_mark_square_out_of_bounds_X(self):
        self.assertFalse(self.board.mark_square(1, 4, 'X'))

    def test_mark_square_out_of_bounds_O(self):
        self.assertFalse(self.board.mark_square(1, 4, 'O'))

    def test_mark_square_out_of_bounds_row_and_col(self):
        self.assertFalse(self.board.mark_square(5, 4, 'X'))

    def test_board_tied_normal_use(self):
        self.board.mark_square(0, 0, 'O')
        self.board.mark_square(0, 1, 'X')
        self.board.mark_square(0, 2, 'X')
        self.board.mark_square(1, 0, 'X')
        self.board.mark_square(1, 1, 'X')
        self.board.mark_square(1, 2, 'O')
        self.board.mark_square(2, 0, 'O')
        self.board.mark_square(2, 1, 'O')
        self.board.mark_square(2, 2, 'X')
        self.assertTrue(self.board.board_tied())

    def test_board_tied_full_invalid(self):
        self.board.mark_square(0, 0, 'O')
        self.board.mark_square(0, 1, 'O')
        self.board.mark_square(0, 2, 'O')
        self.board.mark_square(1, 0, 'O')
        self.board.mark_square(1, 1, 'X')
        self.board.mark_square(1, 2, 'O')
        self.board.mark_square(2, 0, 'O')
        self.board.mark_square(2, 1, 'O')
        self.board.mark_square(2, 2, 'X')
        self.assertFalse(self.board.board_tied())

    def test_board_tied_full_winner_X(self):
        self.board.mark_square(0, 0, 'X')
        self.board.mark_square(0, 1, 'X')
        self.board.mark_square(0, 2, 'X')
        self.board.mark_square(1, 0, 'O')
        self.board.mark_square(1, 1, 'X')
        self.board.mark_square(1, 2, 'O')
        self.board.mark_square(2, 0, 'O')
        self.board.mark_square(2, 1, 'X')
        self.board.mark_square(2, 2, 'O')
        self.assertFalse(self.board.board_tied())

    def test_board_tied_full_winner_O(self):
        self.board.mark_square(0, 0, 'O')
        self.board.mark_square(0, 1, 'O')
        self.board.mark_square(0, 2, 'O')
        self.board.mark_square(1, 0, 'X')
        self.board.mark_square(1, 1, 'O')
        self.board.mark_square(1, 2, 'X')
        self.board.mark_square(2, 0, 'X')
        self.board.mark_square(2, 1, 'O')
        self.board.mark_square(2, 2, 'X')
        self.assertFalse(self.board.board_tied())

    def test_board_tied_not_full(self):
        self.board.mark_square(1, 1, 'X')
        self.board.mark_square(1, 2, 'O')
        self.board.mark_square(2, 0, 'O')
        self.board.mark_square(2, 1, 'X')
        self.board.mark_square(2, 2, 'O')
        self.assertFalse(self.board.board_tied())

    def test_board_valid_correct(self):
        self.board.mark_square(1, 1, 'X')
        self.board.mark_square(1, 2, 'O')
        self.board.mark_square(2, 0, 'O')
        self.assertTrue(self.board.board_valid())

    def test_board_valid_empty(self):
        self.assertTrue(self.board.board_valid())

    def test_board_valid_too_many_X(self):
        self.board.mark_square(1, 1, 'X')
        self.board.mark_square(1, 2, 'X')
        self.board.mark_square(2, 0, 'X')
        self.assertFalse(self.board.board_valid())

    def test_has_winner_tie(self):
        self.board.mark_square(0, 0, 'O')
        self.board.mark_square(0, 1, 'X')
        self.board.mark_square(0, 2, 'X')
        self.board.mark_square(1, 0, 'X')
        self.board.mark_square(1, 1, 'X')
        self.board.mark_square(1, 2, 'O')
        self.board.mark_square(2, 0, 'O')
        self.board.mark_square(2, 1, 'O')
        self.board.mark_square(2, 2, 'X')
        self.assertIsNone(self.board.test_has_winner())

if __name__ == "__main__":
    unittest.main()