""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""

class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: true on sucess, false on error
        """
        if self.out_of_bounds(column, row):
            return False
        if not self.square_empty(column, row):
            return False
        if not self.valid_player(player):
            return False
        self.board[column][row] = player
        return True

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: X, O, or None if no winner
        """

        player = 'X'
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return player

        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return player

        for i in range(3):
            vertical = True
            for j in range(3):
                vertical = vertical and self.board[i][j] == player
            if vertical:
                return player

        for i in range(3):
            horizontal = True
            for j in range(3):
                horizontal = horizontal and self.board[j][i] == player
            if horizontal:
                return player

        player = 'O'
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return player
        
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return player

        for i in range(3):
            vertical = True
            for j in range(3):
                vertical = vertical and self.board[i][j] == player
            if vertical:
                return player

        for i in range(3):
            horizontal = True
            for j in range(3):
                horizontal = horizontal and self.board[j][i] == player
            if horizontal:
                return player

        return None

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        player = 'X'

        while not self.board_full():
            print(self.board)
            print("Current player: " + player)
            valid_input = False
            while not valid_input:
                print("please enter column then row:")
                input_col = int(input())
                input_row = int(input())
                valid_input = self.mark_square(input_col, input_row, player)
                if not valid_input:
                    print("Invalid input, please try again")
            if self.has_winner() is not None:
                return player
            if self.board_tied():
                return None
            
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        return None

    def out_of_bounds(self, column, row):
        """
        Returns true if the space specified by the column and row is out of bounds
        """
        if column < 0 or column >= 3 or row < 0 or row >= 3:
            return True
        return False

    def square_empty(self, column, row):
        """
        Returns true if the space specified by the column and row is empty 
        """
        if self.out_of_bounds(column, row):
            return False
        return self.board[column][row] == '_'

    def board_full(self):
        """
        Returns true if the board is full
        """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    return False

        return True

    def valid_player(self, player):
        """
        Checks whether the player is X or O
        """
        return player == 'X' or player == 'O'

    def board_tied(self):
        """
        Checks whether the board is in a tied state
        Will return true even if the board has been won
        """
        return self.board_full() and self.board_valid()

    def board_valid(self):
        """
        Checks if the board has the correct number of X and O values
        """
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X':
                    x_count += 1
                elif self.board[i][j] == 'O':
                    o_count += 1
        return abs(x_count - o_count) <= 1
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))