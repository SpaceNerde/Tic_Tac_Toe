# This is Tic Tac Toe Based on Text running in the Terminal
# Basic Tic Tac Toe Rules and Features

ttt_map = ([[" ", "|", " ", "|", " "],  # 0:0 | 2:0 | 4:0
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", " ", "|", " "],  # 0:2 | 2:2 | 4:2
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", " ", "|", " "]]) # 0:4 | 2:4 | 4:4

def run():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in ttt_map]))