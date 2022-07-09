"""
Game Legend
'X' for a hit on a battleship
' ' for an available space on the game board
'-' for a missed shot on the game board
"""

from random import randint

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


# User input for shot location
def guess_ship_location():
    row = input('Argh! What be the longitude to fire upon? Pick a row 1-8:\n')
    while row not in '12345678':
        print('These be bad coordinates, try again!\n')
        row = input('What be the longitude to fire upon? Pick a row, 1-8:\n')

    column = input('Avast! Now the latitude! Pick a column A-H:\n').upper()
    while column not in 'ABCDEFGH':
        print('This is out of our range, try again between A-H!:\n')
        column = input('Avast! Now the latitude! Pick a column A-H:\n').upper()

    return int(row) - 1, letters_to_numbers[column]


# Checks if shot hit or missed
def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(player_board)
turns = 10
while turns > 0:
    print('Ahoy matey! Welcome to battleship!\n')
    print_board(computer_board)
    row, column = guess_ship_location()

    if computer_board[row][column] == '-':
        print('Argh, you already shot there! Try again!')

    elif player_board[row][column] == 'X':
        print('Shiver me timbers! That be a hit matey!')
        computer_board[row][column] = 'X'
        turns -= 1

    else:
        print('That be a missed shot ya scallywag!')
        computer_board[row][column] = '-'
        turns -= 1

    if count_hits(computer_board) == 5:
        print('Congratulations! You be a real pirate captain! All ships sunk!')
        break

    print('You have ' + str(turns) + ' turns remaining')

    if turns == 0:
        print('You ran out of shots, luck be with you next time!')
        break