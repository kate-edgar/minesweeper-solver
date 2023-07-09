# Solves a given board

import Board
from Board import board


def check_mine(board, rows, columns):
    available_spaces = []
    for i in range(rows):
        for j in range(columns):
            if board[i][j] != 0 and board[i][j] != 'y':
                available_spaces.append(board[i][j])
                potential_mine = search_area(i, j, rows, columns, 'y')
                if len(potential_mine) == board[i][j]:
                    board[potential_mine[0][0]][potential_mine[0][1]] = 'X'


def check_safe(board, rows, columns):
    num_mines = []
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 'y':
                num_mines = search_area(i, j, rows, columns, 'y')
                print(num_mines)
                if len(num_mines) == board[i][j]:
                    pass


def top_left(x, y, search):
    if board[x-1][y-1] == search:
        return x - 1, y - 1


def top_middle(x, y, search):
    if board[x][y-1] == search:
        return x, y - 1


def top_right(x, y, search):
    if board[x+1][y-1] == search:
        return x + 1, y - 1


def middle_left(x, y, search):
    if board[x-1][y] == search:
        return x - 1, y


def middle_right(x, y, search):
    if board[x+1][y] == search:
        return x + 1, y


def bottom_left(x, y, search):
    if board[x-1][y+1] == search:
        return x - 1, y + 1


def bottom_middle(x, y, search):
    if board[x][y+1] == search:
        return x, y + 1


def bottom_right(x, y, search):
    if board[x+1][y+1] == search:
        return x + 1, y + 1


def search_area(x, y, num_rows, num_col, search):
    potential_mines = []

    # Case 1: Top left corner
    if y == 0 and x == 0:
        potential_mines.append(middle_right(x, y, search))
        potential_mines.append(bottom_right(x, y, search))
        potential_mines.append(bottom_middle(x, y, search))

    # Case 2: Top right corner
    elif y == 0 and x == num_rows-1:
        potential_mines.append(middle_left(x, y, search))
        potential_mines.append(bottom_left(x, y, search))
        potential_mines.append(bottom_middle(x, y, search))

    # Case 3: Bottom left corner
    elif y == num_col - 1 and x == 0:
        potential_mines.append(top_middle(x, y, search))
        potential_mines.append(top_right(x, y, search))
        potential_mines.append(middle_right(x, y, search))

    # Case 4: Bottom right corner
    elif y == num_col-1 and x == num_rows-1:
        potential_mines.append(top_left(x, y, search))
        potential_mines.append(top_middle(x, y, search))
        potential_mines.append(middle_left(x, y, search))

    # Case 5: Against Left
    elif x == 0:
        potential_mines.append(top_middle(x, y, search))
        potential_mines.append(top_right(x, y, search))
        potential_mines.append(middle_right(x, y, search))
        potential_mines.append(bottom_right(x, y, search))
        potential_mines.append(bottom_middle(x, y, search))

    # Case 2: Against Top
    elif y == 0:
        potential_mines.append(middle_left(x, y, search))
        potential_mines.append(middle_right(x, y, search))
        potential_mines.append(bottom_left(x, y, search))
        potential_mines.append(bottom_middle(x, y, search))
        potential_mines.append(bottom_right(x, y, search))

    # Case 3: Against Bottom
    elif y == num_col-1:
        potential_mines.append(top_left(x, y, search))
        potential_mines.append(top_middle(x, y, search))
        potential_mines.append(top_right(x, y, search))
        potential_mines.append(middle_left(x, y, search))
        potential_mines.append(middle_right(x, y, search))

    # Case 4: Against Right
    elif x == num_rows-1:
        potential_mines.append(top_left(x, y, search))
        potential_mines.append(top_middle(x, y, search))
        potential_mines.append(middle_left(x, y, search))
        potential_mines.append(bottom_left(x, y, search))
        potential_mines.append(bottom_middle(x, y, search))

    # Case 9: Middle
    else:
        potential_mines.append(top_left(x, y, search))
        potential_mines.append(top_middle(x, y, search))
        potential_mines.append(top_right(x, y, search))
        potential_mines.append(middle_left(x, y, search))
        potential_mines.append(middle_right(x, y, search))
        potential_mines.append(bottom_left(x, y, search))
        potential_mines.append(bottom_middle(x, y, search))
        potential_mines.append(bottom_right(x, y, search))

    new_potential_mines = list(filter(None, potential_mines))
    return new_potential_mines


columns = 10
rows = 8

board = board()
# Board.print_grid(2, 3)

print("Starting board:")
Board.print_board(board, rows)

check_mine(board, rows, columns)
check_safe(board, rows, columns)

print('Solution:')
Board.print_board(board, rows)
