import random

class TicTacToe():
    """This a class for tic_tac_toe game.
    in this class we have different methods.
    List of Methods:
    - get_random_first_player 
    - fix_spot
    - has_player_won
    - is_board_fill
    - swap_player_turn
    - show_board
    - start
    """

    def __init__(self):
        self.board = [' '] * 10 # we don't use 0 index
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        """Choose the first player randomly.

        :return: 'X' or 'O'
        :rtype: str
        """
        return random.choice(['X','O'])
    
    def fix_spot(self, cell: int, player: str):
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        """Tell us the current player win or not yet.

        :param player: The player 'X' or 'O'
        :return: True or False
        """
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),
                            (1, 5, 9), (3, 5, 7)]
        
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == player:
                return True
        return False

    def is_board_filled(self) -> bool:
        """Tell us that board is fill or not. If the board is fill, 
        we should stop the game and print the winner or Draw.

        :return: True or Fasle
        :rtype: bool
        """
        return ' ' not in self.board[1:10]
    
    def swap_player_turn(self):
        """In each turn, we should swap the player automatically. This function do this
        for us.
        """
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
    
    def show_board(self):
        """This function show board for us in each turn.
        """
        print("\n")
        print('-------------')
        rows = [[self.board[i+j] for i in range(1, 4)] for j in range(0, 7, 3)]
        for row in rows:
            print('| ' + row[0] + ' | ' + row[1] + ' | ' + row[2] + ' | ')
            print('-------------')

        print("\n")

    def start(self):
        """After making an instance from our class, we call this method to
        run the game.
        """
        while True:
            self.show_board()
            try:
                cell = int(input(f"Player {self.player_turn}, Enter the cell number: "))

                 # Check if cell is in the allowed range and is empty.
                if cell in range(1, 10) and self.board[cell] == ' ':
                    self.fix_spot(cell, self.player_turn)

                    if self.has_player_won(self.player_turn):
                        self.show_board()
                        print(f"Player {self.player_turn} wins!")
                        break

                    if self.is_board_filled():
                        self.show_board()
                        print("It's a Draw!")
                        break

                    self.swap_player_turn()
                else:
                    print('Invalid input, please try again!')
                
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")


if __name__ == '__main__':
    # Create a game and start it
    game = TicTacToe()
    game.start()



                
