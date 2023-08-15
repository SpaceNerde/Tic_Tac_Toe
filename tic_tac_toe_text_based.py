# This is Tic Tac Toe Based on Text running in the Terminal
# Basic Tic Tac Toe Rules and Features
from nltk import pr

# x:y

ttt_map = ([[" ", "|", " ", "|", " "],  # 0:0 | 2:0 | 4:0
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", "O", "|", " "],  # 0:2 | 2:2 | 4:2
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", " ", "|", " "]]) # 0:4 | 2:4 | 4:4

def run():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in ttt_map]))

def print_coordination_data(x, y):
    if not isinstance(x and y, int):
        return print("ERROR: You have to choose two integers as x and y")

    print(x, y)
