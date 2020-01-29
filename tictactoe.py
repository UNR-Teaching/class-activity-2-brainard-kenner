""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""

class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_']*3]*3 

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: true on sucess, false on error
        """

        pass

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: X, O, or None if no winner
        """

        pass

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        
        pass

    def out_of_bounds(self, column, row):
        """
        Returns true if the space specified by the column and row is out of bounds
        """
        pass

    def square_empty(self, column, row):
        """
        Returns true if the space specified by the column and row is empty 
        """
        pass

    def board_full(self):
        """
        Returns true if the board is full
        """
        pass

        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))