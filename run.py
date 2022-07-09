"""
Game Legend
'X' for a hit on a battleship
' ' for an available space on the game board
'-' for a missed shot on the game board
"""


# Board for user ship locations
player_board = [[" "] * 8 for x in range(8)]

# Board for computer ship locations
computer_board = [[" "] * 8 for x in range(8)]

letters_to_numbers = {
    'A': 0, 'B': 1,
    'C': 2, 'D': 3,
    'E': 4, 'F': 5,
    'G': 6, 'H': 7
    }


# Creates the layout of the game board
def print_board(board):
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d | %s |" % (row_number, "|".join(row)))
        row_number += 1


# Creates 5 ships at random positions on the board
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


def guess_ship_location():
    pass


def count_hits():
    pass


create_ships()
turns = 10
# while turns > 0:
