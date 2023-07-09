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
                search_area(i, j, rows, columns)
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

    # Case 1: Against Left
    if y == 0:
        top_middle(x, y)
        top_right(x, y)
        middle_right(x, y)
        bottom_right(x, y)
        bottom_middle(x, y)
        
    # Case 2: Against Top
    elif x == 0:
        middle_left(x, y)
        middle_right(x, y)
        bottom_left(x, y)
        bottom_middle(x, y)
        bottom_right(x, y)
        
    # Case 3: Against Bottom
    elif y == num_col-1:
        top_left(x, y)
        top_middle(x, y)
        top_right(x, y)
        middle_left(x, y)
        middle_right(x, y)
        
    # Case 4: Against Right
    elif x == num_rows-1:
        top_left(x, y)
        top_middle(x, y)
        middle_left(x, y)
        bottom_left(x, y)
        bottom_middle(x, y)
        
    # Case 5: No Edge
    else:
        top_left(x, y)
        top_middle(x, y)
        top_right(x, y)
        middle_left(x, y)
        middle_right(x, y)
        bottom_left(x, y)
        bottom_middle(x, y)
        bottom_right(x, y)
        
    return potential_bombs


print(search_space(board, rows, columns))
