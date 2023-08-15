# This is Tic Tac Toe Based on Text running in the Terminal
# Basic Tic Tac Toe Rules and Features
from nltk import pr

# x:y

ttt_map = ([[" ", "|", " ", "|", " "],  # 1:1 | 3:1 | 5:1
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", "O", "|", " "],  # 1:3 | 3:3 | 5:3
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", " ", "|", " "]]) # 1:5 | 3:5 | 5:5

def get_player():
    player = input("Please Choose if you are X or O\n"
                   ">> ")
    return player

def run():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in ttt_map]))

    print("\nThis is the state of the board\n")

    player = get_player()
    if not player in ("O", "X"):
        print("\nYou have to choose between X and O")
        player = get_player()

    print("\nYou are Player " + player)

def print_coordination_data(x, y):
    if not isinstance(x and y, int):
        return print("ERROR: You have to choose two integers as x and y")

    print(ttt_map[-x][-y])
