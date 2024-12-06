import numpy as np

class Game:
    def __init__(self):
        # use NumPy create a 3x3 board
        self.board = np.full((3, 3), " ")  # initialize the board as 3x3
        self.current_player = "X"  # player X starts first

    def display_board(self):
        # print board
        print(self.board)
        print("-" * 5)

    def make_move(self, x, y):
        # put chess on the board
        if self.board[x, y] == " ":
            self.board[x, y] = self.current_player
            return True
        return False

    def is_full(self):
        # check whether the board is full
        return not np.any(self.board == " ")

    def check_winner(self):
        # Check rows, columns, and diagonals for winners
        for i in range(3):
            # check line
            if np.all(self.board[i, :] == self.current_player):
                return self.current_player
            # check list
            if np.all(self.board[:, i] == self.current_player):
                return self.current_player

        # check diagonal
        if np.all(np.diagonal(self.board) == self.current_player):
            return self.current_player
        if np.all(np.diagonal(np.fliplr(self.board)) == self.current_player):
            return self.current_player

        return None

    def get_move(self):
        while True:
            try:
                move = input(f"Player {self.current_player}, please enter your move (row,col): ")
                x, y = map(int, move.split(","))
                if 0 <= x < 3 and 0 <= y < 3:
                    return x, y
                else:
                    print("Invalid input! Please enter values between 0 and 2.")
            except ValueError:
                print("Invalid format! Please enter in the form row,col (e.g., 1,2).")

    def run(self):
        while True:
            self.display_board()
            x, y = self.get_move()

            if self.make_move(x, y):
                winner = self.check_winner()
                if winner:
                    print(f"\nPlayer {winner} wins!")
                    self.display_board()
                    break
                elif self.is_full():
                    print("\nIt's a draw!")
                    self.display_board()
                    break

                # switch player
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                print("That square is already taken! Try again.")

# run the game
game = Game()
game.run()
