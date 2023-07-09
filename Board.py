# Generates a randomized board

# Board dimensions
columns = 10
rows = 8
board = [[0 for column in range(columns)] for row in range(rows)]

# Test case
# 0 = Grey space
# x = Bomb marker
# y = Empty space
testBoard = [[0, 0, 2, 0, 0, 0, 0, 0, 0, 0],[0, 0, 3, 0, 0, 0, 0, 0, 1, 1],[2, 0, 2, 0, 0, 0, 0, 0, 2, 0],[1, 1, 1, 0, 0, 0, 1, 1, 3, 0],[0, 0, 0, 0, 0, 0, 1, 0, 2, 1],[0, 0, 0, 0, 1, 1, 2, 1, 2, 1],[0, 1, 1, 1, 1, 0, 2, 1, 1, 0],[0, 1, 0, 1, 1, 2, 0, 1, 1, 1]]

for i in range(rows):
    print(testBoard[i])
