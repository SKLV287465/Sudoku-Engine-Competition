import sys

def is_complete(board):
    for x in range(9):
        for y in range(9):
            if (board[x][y] == 0):
                return False
    return True

def is_correct(board):
    # check every row
    
    # check every column
    
    #check every box


board = [[0] * 9] * 9


for x in range(1, len(sys.argv)):
    group = sys.argv[x]
    board[int(sys.argv[x][0])][int(sys.argv[x][1])] = int(sys.argv[x][2])


        