"""
Game Legend
'X' for a hit on a battleship
' ' for an available space on the game board
'-' for a missed shot on the game board
"""

from random import randint

# Global variable for number of ships
SHIPS = 5
# Global variable for total number of turns
TURNS = 8

# Board for user ship locations, holds ship positions
player_board = [[" "] * 7 for x in range(7)]

# Board for player shots, shows hits and misses
hidden_board = [[" "] * 7 for x in range(7)]

letters_to_numbers = {
    'A': 0, 'B': 1,
    'C': 2, 'D': 3,
    'E': 4, 'F': 5,
    'G': 6
    }


def print_board(board):
    """
    Creates the layout of the game board
    """
    print('    A B C D E F G')
    print('  +--+-+-+-+-+--+')
    row_number = 1
    for row in board:
        print("%d | %s |" % (row_number, "|".join(row)))
        row_number += 1
    print('  +--+-+-+-+-+--+')


def create_ships(board):
    """
    Creates 5 ships at random positions on the board
    """
    for _ in range(SHIPS):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 6), randint(0, 6)
        board[ship_row][ship_column] = 'X'


def guess_ship_location():
    """
    User input for shot location
    """
    row = input('Argh! What be the latitude to fire upon? Pick a row 1-7:\n')
    while row not in '1234567':
        print('These be bad coordinates, try again!\n')
        row = input('What be the latitude to fire upon? Pick a row, 1-7:\n')

    column = input('Argh! Now the longitude! Pick a column A-G:\n').upper()
    while column not in 'ABCDEFG':
        print('This is out of our range, try again between A-G!:\n')
        column = input('Argh! Now the longitude! Pick a column A-G:\n').upper()

    return int(row) - 1, letters_to_numbers[column]


def count_hits(board):
    """
    Checks if shot hit or missed
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def difficulty():
    """
    User input for difficulty setting
    """
    answer = input("Select 1 for Easy or 2 for Difficult: ")
    if answer == '1':
        print('Easy mode selected! You have 8 turns.')
    elif answer == '2':
        print('Difficult mode selected! You have 5 turns.')
        global TURNS
        TURNS = 5
    else:
        print("You didn't pick 1 or 2, try again.")
        difficulty()


def new_game():
    """
    Starts a new game
    """
    create_ships(player_board)
    turns_taken = 0
    while turns_taken < TURNS:

        if turns_taken == 0:
            print('Ahoy matey! Welcome to battleship!\n')
            difficulty()
            print_board(hidden_board)
            row, column = guess_ship_location()

        else:
            print_board(hidden_board)
            row, column = guess_ship_location()

        if hidden_board[row][column] == '-':
            print('Argh, you already shot there! Try again!')

        elif player_board[row][column] == 'X':
            print('Shiver me timbers! That be a hit matey!')
            hidden_board[row][column] = 'X'
            turns_taken += 1

        else:
            print('That be a missed shot ya scallywag!')
            hidden_board[row][column] = '-'
            turns_taken += 1

        if count_hits(hidden_board) == 5:
            print('Congrats! You be a real pirate captain! All ships sunk!')
            break

        print('You have ' + str(TURNS - turns_taken) + ' turns remaining')

        if turns_taken == TURNS:
            print('You ran out of shots, luck be with you next time!')
            break


if __name__ == "__main__":
    new_game()
