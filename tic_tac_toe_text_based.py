# This is Tic Tac Toe Based on Text running in the Terminal
# Basic Tic Tac Toe Rules and Features

# x:y

ttt_map = ([[" ", "|", " ", "|", " "],  # 5:5 | 5:3 | 5:1
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", " ", "|", " "],  # 3:5 | 3:3 | 3:1
            ["_", "+", "_", "+", "_"],  #
            [" ", "|", " ", "|", " "]]) # 1:5 | 1:5 | 1:1

ttt_map_player_positions = \
          ([["1", "|", "2", "|", "3"],  # 5:5 | 5:3 | 5:1
            ["_", "+", "_", "+", "_"],  #
            ["4", "|", "5", "|", "6"],  # 3:5 | 3:3 | 3:1
            ["_", "+", "_", "+", "_"],  #
            ["7", "|", "8", "|", "9"]]) # 1:5 | 1:3 | 1:1

def big_shity_if_block(INPUT, player):
    if INPUT == 1:
        ttt_map[-5][-5] = player
    elif INPUT == 2:
        ttt_map[-5][-3] = player
    elif INPUT == 3:
        ttt_map[-5][-1] = player
    elif INPUT == 4:
        ttt_map[-3][-5] = player
    elif INPUT == 5:
        ttt_map[-3][-3] = player
    elif INPUT == 6:
        ttt_map[-3][-1] = player
    elif INPUT == 7:
        ttt_map[-1][-5] = player
    elif INPUT == 8:
        ttt_map[-1][-3] = player
    elif INPUT == 9:
        ttt_map[-1][-1] = player

def get_player():
    player = input("Please Choose if you are X or O\n"
                   ">> ").upper()
    if not player in ("O", "X"):
        print("\nYou have to choose between X and O")
        return get_player()
    return player

def edit_coordination(player):
    print("\nPick between 1 and 9 to place your "+player)

    try:
        pos = int(input("\nchoose position: "))
    except ValueError:
        print("\nYou have to pick a integer as position")
        return edit_coordination(player)

    big_shity_if_block(pos, player)

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in ttt_map]))

def run():
    print("\n")

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in ttt_map]))

    print("\n")

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in ttt_map_player_positions]))

    print("\nThis is the state of the board\n")

    player = get_player()

    print("\nYou are Player " + player)

    print("\n it is your turn player ")
    edit_coordination(player)

def print_coordination_data(x, y):
    if not isinstance(x and y, int):
        return print("ERROR: You have to choose two integers as x and y")

    print(ttt_map[-x][-y])
