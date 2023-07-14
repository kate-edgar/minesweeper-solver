# Generates a game
import random

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
    return board


def define_nums(board, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if board[i][j] != 'B':
                num_mines = search_area(board, i, j, rows, columns, 'B')
                board[i][j] = len(num_mines)
    return board


def print_board(board, rows):
    for i in range(rows):
        print(board[i])


def top_left(board, x, y, search):
    if board[x-1][y-1] == search:
        return x - 1, y - 1


def top_middle(board, x, y, search):
    if board[x][y-1] == search:
        return x, y - 1


def top_right(board, x, y, search):
    if board[x+1][y-1] == search:
        return x + 1, y - 1


def middle_left(board, x, y, search):
    if board[x-1][y] == search:
        return x - 1, y


def middle_right(board, x, y, search):
    if board[x+1][y] == search:
        return x + 1, y


def bottom_left(board, x, y, search):
    if board[x-1][y+1] == search:
        return x - 1, y + 1


def bottom_middle(board, x, y, search):
    if board[x][y+1] == search:
        return x, y + 1


def bottom_right(board, x, y, search):
    if board[x+1][y+1] == search:
        return x + 1, y + 1


def search_area(board, x, y, num_rows, num_col, search):
    potential_mines = []

    # Case 1: Top left corner
    if y == 0 and x == 0:
        potential_mines.append(middle_right(board, x, y, search))
        potential_mines.append(bottom_right(board, x, y, search))
        potential_mines.append(bottom_middle(board, x, y, search))

    # Case 2: Top right corner
    elif y == 0 and x == num_rows-1:
        potential_mines.append(middle_left(board, x, y, search))
        potential_mines.append(bottom_left(board, x, y, search))
        potential_mines.append(bottom_middle(board, x, y, search))

    # Case 3: Bottom left corner
    elif y == num_col - 1 and x == 0:
        potential_mines.append(top_middle(board, x, y, search))
        potential_mines.append(top_right(board, x, y, search))
        potential_mines.append(middle_right(board, x, y, search))

    # Case 4: Bottom right corner
    elif y == num_col-1 and x == num_rows-1:
        potential_mines.append(top_left(board, x, y, search))
        potential_mines.append(top_middle(board, x, y, search))
        potential_mines.append(middle_left(board, x, y, search))

    # Case 5: Against Left
    elif x == 0:
        potential_mines.append(top_middle(board, x, y, search))
        potential_mines.append(top_right(board, x, y, search))
        potential_mines.append(middle_right(board, x, y, search))
        potential_mines.append(bottom_right(board, x, y, search))
        potential_mines.append(bottom_middle(board, x, y, search))

    # Case 2: Against Top
    elif y == 0:
        potential_mines.append(middle_left(board, x, y, search))
        potential_mines.append(middle_right(board, x, y, search))
        potential_mines.append(bottom_left(board, x, y, search))
        potential_mines.append(bottom_middle(board, x, y, search))
        potential_mines.append(bottom_right(board, x, y, search))

    # Case 3: Against Bottom
    elif y == num_col-1:
        potential_mines.append(top_left(board, x, y, search))
        potential_mines.append(top_middle(board, x, y, search))
        potential_mines.append(top_right(board, x, y, search))
        potential_mines.append(middle_left(board, x, y, search))
        potential_mines.append(middle_right(board, x, y, search))

    # Case 4: Against Right
    elif x == num_rows-1:
        potential_mines.append(top_left(board, x, y, search))
        potential_mines.append(top_middle(board, x, y, search))
        potential_mines.append(middle_left(board, x, y, search))
        potential_mines.append(bottom_left(board, x, y, search))
        potential_mines.append(bottom_middle(board, x, y, search))

    # Case 9: Middle
    else:
        potential_mines.append(top_left(board, x, y, search))
        potential_mines.append(top_middle(board, x, y, search))
        potential_mines.append(top_right(board, x, y, search))
        potential_mines.append(middle_left(board, x, y, search))
        potential_mines.append(middle_right(board, x, y, search))
        potential_mines.append(bottom_left(board, x, y, search))
        potential_mines.append(bottom_middle(board, x, y, search))
        potential_mines.append(bottom_right(board, x, y, search))


    # Main
    new_potential_mines = list(filter(None, potential_mines))
    return new_potential_mines


board = place_mines(rows, columns, num_mines)
board = define_nums(board, rows, columns)
print()
print_board(board, rows)
