import numpy as np

# enums for player 1 and player 2
PLAYER1 = 1
PLAYER2 = 2

# our "game" object class
class GameClass:
    def __init__(self):
        self.board = np.zeros((3,3))
    
    # function to make a move in the game
    def make_move(self, row, col, player):
        if (row > 2 or row < 0 or col < 0 or col > 2 or player < 1 or player > 2):
            print("Bad input!")
            return
        if self.board[row][col] == 0:
            self.board[row][col] = player
        else:
            print("Spot already filled!")
    
    # checks if a player has won
    def win_condition(self, player):
        streak = 0
        if self.board[1][1] == player:
            if self.board[0][0] == player:
                if self.board[2][2] == player:
                    print(str(player) + " wins (first diagonal)!")
                    quit()
            if self.board[0][2] == player:
                if self.board[2][0] == player:
                    print(str(player) + " wins (second diagonal)!")
                    quit()
        for row in self.board:
            if row[0] == player:
                streak += 1
                for i in range(1,3):
                    if row[i] == player:
                        streak += 1
                if streak == 3:
                    print(str(player) + " wins (row)!")
                    quit()
            streak = 0
        for i in range(3):
            if self.board[0][i] == player:
                streak += 1
                for j in range(1,3):
                    if self.board[j][i] == player:
                        streak += 1
                if streak == 3:
                    print(str(player) + " wins (col)!")
                    quit()
            streak = 0
        print("No winner yet")
    
    # prints the current board
    def print_board(self):
        to_print = np.copy(self.board)
        print("-------------")
        for row in to_print:
            print('|', end = "")
            for i in range(3):
                if row[i] == 1:
                    print(' X |', end = "")
                elif row[i] == 2:
                    print(' O |', end = "")
                else:
                    print('   |', end = "")
            print('')
            print("-------------")

if __name__ == "__main__":
    # create our game object
    ttt = GameClass()

    # create our visited states as a python set
    visited_states = set()

    # print the initial board
    ttt.print_board()

    # play loop
    while(True):
        # getting input
        print("Make a move (row, col, player): ")
        r = input()
        if r == 'q':
            quit()
        col = input()
        player = input()

        # making moves based on input
        ttt.make_move(int(r), int(col), int(player))
        state = ttt.board.tobytes()
        if state not in visited_states:
            visited_states.add(state)
        ttt.print_board()

        # checking if either player won yet
        ttt.win_condition(PLAYER1)
        ttt.win_condition(PLAYER2)
    pass