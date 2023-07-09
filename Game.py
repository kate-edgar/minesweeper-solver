# Generates a game

# Generates a game
import random
import random as rand

# Board specs
num_mines = 10
columns = 10
rows = 8


def empty_board(rows, columns):
    board = [[0 for column in range(columns)] for row in range(rows)]
    return board


def place_mines(rows, columns, num_mines):
    board = empty_board(rows, columns)
    for i in range(num_mines):
        x = random.randint(0, rows-1)
        y = random.randint(0, columns-1)
        board[x][y] = 'B'
    print_board(board, rows)


def print_board(board, rows):
    for i in range(rows):
        print(board[i])

place_mines(rows, columns, num_mines)
