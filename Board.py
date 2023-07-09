# Generates a randomized board

def board():
    # Board dimensions
    columns = 10
    rows = 8
    board = [[0 for column in range(columns)] for row in range(rows)]

    # Test case
    # 0 = Grey space
    # x = Bomb marker
    # y = Empty space
    testBoard = [['y', 'y', 2, 0, 0, 0, 0, 0, 0, 0],['y', 'y', 3, 0, 0, 0, 0, 0, 1, 1],[2, 'y', 2, 0, 0, 0, 0, 0, 2, 'y'],[1, 1, 1, 0, 0, 0, 1, 1, 3, 'y'],[0, 0, 0, 0, 0, 0, 1, 'y', 2, 1],[0, 0, 0, 0, 1, 1, 2, 1, 2, 1],[0, 1, 1, 1, 1, 'y', 2, 1, 1, 'y'],[0, 1, 'y', 1, 1, 2, 'y', 1, 1, 1]]

    return testBoard


def print_board(board, rows):
    for i in range(rows):
        print(board[i])


# Testing
def print_grid(x, y):
    for i in range(x):
        for j in range(y):
            print('+', '-', '+')
            print(('|'+ ' '*y)*(y-1))
