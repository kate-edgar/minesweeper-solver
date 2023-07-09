import Board
from Board import board

columns = 10
rows = 8

board = board()
# Board.print_grid(2, 3)

Board.print_board(board, rows)


def search_space(board, rows, columns):
    available_spaces = []
    for i in range(rows):
        for j in range(columns):
            if board[i][j] != 0 and board[i][j] != 'y':
                available_spaces.append(board[i][j])
                potential_bomb = search_area(i, j, rows, columns)
                if len(potential_bomb) == board[i][j]:
                    print(potential_bomb)
                    board[potential_bomb[0][0]][potential_bomb[0][1]] = 'X'
    return available_spaces


def top_left(x, y):
    if board[x-1][y-1] == 'y':
        return x - 1, y - 1


def top_middle(x, y):
    if board[x][y-1] == 'y':
        return x, y - 1


def top_right(x, y):
    if board[x+1][y-1] == 'y':
        return x + 1, y - 1


def middle_left(x, y):
    if board[x-1][y] == 'y':
        return x - 1, y


def middle_right(x, y):
    if board[x+1][y] == 'y':
        return x + 1, y


def bottom_left(x, y):
    if board[x-1][y+1] == 'y':
        return x - 1, y + 1


def bottom_middle(x, y):
    if board[x][y+1] == 'y':
        return x, y + 1


def bottom_right(x, y):
    if board[x+1][y+1] == 'y':
        return x + 1, y + 1


def search_area(x, y, num_rows, num_col):
    potential_bombs = []

    # Case 1: Top left corner
    if y == 0 and x == 0:
        potential_bombs.append(middle_right(x, y))
        potential_bombs.append(bottom_right(x, y))
        potential_bombs.append(bottom_middle(x, y))

    # Case 2: Top right corner
    elif y == 0 and x == num_rows-1:
        potential_bombs.append(middle_left(x, y))
        potential_bombs.append(bottom_left(x, y))
        potential_bombs.append(bottom_middle(x, y))

    # Case 3: Bottom left corner
    elif y == num_col - 1 and x == 0:
        potential_bombs.append(top_middle(x, y))
        potential_bombs.append(top_right(x, y))
        potential_bombs.append(middle_right(x, y))

    # Case 4: Bottom right corner
    elif y == num_col-1 and x == num_rows-1:
        potential_bombs.append(top_left(x, y))
        potential_bombs.append(top_middle(x, y))
        potential_bombs.append(middle_left(x, y))

    # Case 5: Against Left
    elif x == 0:
        potential_bombs.append(top_middle(x, y))
        potential_bombs.append(top_right(x, y))
        potential_bombs.append(middle_right(x, y))
        potential_bombs.append(bottom_right(x, y))
        potential_bombs.append(bottom_middle(x, y))

    # Case 2: Against Top
    elif y == 0:
        potential_bombs.append(middle_left(x, y))
        potential_bombs.append(middle_right(x, y))
        potential_bombs.append(bottom_left(x, y))
        potential_bombs.append(bottom_middle(x, y))
        potential_bombs.append(bottom_right(x, y))

    # Case 3: Against Bottom
    elif y == num_col-1:
        potential_bombs.append(top_left(x, y))
        potential_bombs.append(top_middle(x, y))
        potential_bombs.append(top_right(x, y))
        potential_bombs.append(middle_left(x, y))
        potential_bombs.append(middle_right(x, y))

    # Case 4: Against Right
    elif x == num_rows-1:
        potential_bombs.append(top_left(x, y))
        potential_bombs.append(top_middle(x, y))
        potential_bombs.append(middle_left(x, y))
        potential_bombs.append(bottom_left(x, y))
        potential_bombs.append(bottom_middle(x, y))

    # Case 9: Middle
    else:
        potential_bombs.append(top_left(x, y))
        potential_bombs.append(top_middle(x, y))
        potential_bombs.append(top_right(x, y))
        potential_bombs.append(middle_left(x, y))
        potential_bombs.append(middle_right(x, y))
        potential_bombs.append(bottom_left(x, y))
        potential_bombs.append(bottom_middle(x, y))
        potential_bombs.append(bottom_right(x, y))

    new_potential_bombs = list(filter(None, potential_bombs))
    return new_potential_bombs


print(search_space(board, rows, columns))
Board.print_board(board, rows)
