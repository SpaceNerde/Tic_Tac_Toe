# This is Tic Tac Toe Based on Text running in the Terminal
# Basic Tic Tac Toe Rules and Features

# x:y

ttt_map = ([[" ", "|", " ", "|", " "],  # 1:1 | 3:1 | 5:1
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", "O", "|", " "],  # 1:3 | 3:3 | 5:3
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", " ", "|", "1"]]) # 1:5 | 3:5 | 5:5

valid_inputs = ([[1, 1],
                 [3, 1],
                 [5, 1],
                 [1, 3],
                 [3, 3],
                 [5, 3],
                 [1, 5],
                 [3, 5],
                 [5, 5]])

def check_for_valid_input(x, y):
    if [x, y] in valid_inputs:
        return True
    else:
        return False

def get_player():
    player = input("Please Choose if you are X or O\n"
                   ">> ")
    return player

def edit_coordination(player):
    print("\nPick x and y coordination to place your "+player)

    try:
        x = int(input("\nx: "))
        y = int(input("y: "))
    except ValueError:
        print("\nYou have to pick two integers as coordination's")
        return edit_coordination(player)

    if check_for_valid_input(x, y):
        print_coordination_data(x, y)

def run():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in ttt_map]))

    print("\nThis is the state of the board\n")

    player = get_player()
    if not player in ("O", "X"):
        print("\nYou have to choose between X and O")
        player = get_player()

    print("\nYou are Player " + player)

    edit_coordination(player)

def print_coordination_data(x, y):
    if not isinstance(x and y, int):
        return print("ERROR: You have to choose two integers as x and y")

    print(ttt_map[-x][-y])
