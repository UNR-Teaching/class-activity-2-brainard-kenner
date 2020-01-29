import unittest
from tictactoe import Board

class TicTacToeTester(unittest.TestCase):
    
    def test_row_out_of_bounds(self):
        self.assertTrue(self.board.out_of_bounds(0, 3))
    
    def test_col_out_of_bounds(self):
        self.assertTrue(self.board.out_of_bounds(3, 0))

    def test_row_col_in_bounds(self):
        self.assertFalse(self.board.out_of_bounds(0, 0))

    def test_empty_square(self):
        self.assertTrue(self.board.square_empty(0, 0))

    def test_non_empty_square(self):
        self.board.mark_square(0, 0, 'O')
        self.assertFalse(self.board.square_empty(0, 0))

    def test_board_full(self):
        for i in range(3):
            for j in range(3):
                self.board.mark_square(i, j, 'O')
        self.assertTrue(self.board.board_full())

    def test_board_not_full(self):
        for i in range(3):
            self.board.mark_square(i, i, 'O')
        self.assertFalse(self.board.board_full())

    def test_valid_player_x(self):
        self.assertTrue(self.board.valid_player('X'))

    def test_valid_player_o(self):
        self.assertTrue(self.board.valid_player('O'))

    def test_invalid_player(self):
        self.assertFalse(self.board.valid_player('G'))

    def test_has_winner_diagonal(self):
        for i in range(3):
            self.board.mark_square(i, i, 'X')
        self.assertEqual(self.has_winner(), 'X')

    def test_has_winner_horizontal(self):
        for i in range(3):
            self.board.mark_square(i, 0, 'X')
        self.assertEqual(self.has_winner(), 'X')

    def test_has_winner_vertical(self):
        for i in range(3):
            self.board.mark_square(0, i, 'X')
        self.assertEqual(self.has_winner(), 'X')

    def test_has_no_winner(self):
        self.board.mark_square(0, 0, 'X')
        self.board.mark_square(1, 1, 'O')
        self.board.mark_square(2, 2, 'X')
        self.assertIsNone(self.has_winner())

    def test_has_no_winner_empty_board(self):
        self.assertIsNone(self.has_winner())

if __name__ == "__main__":
    unittest.main()