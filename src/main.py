import sys
import collections

def is_complete(board):
    for x in range(9):
        for y in range(9):
            if (board[x][y] == 0):
                return False
    return True

def is_correct(board):
    # check every row
    for i in range(9):
        row = [0] * 9
        column = [0] * 9
        for j in range(9):
            row[board[i][j]] += 1
            column[board[j][i]] += 1
        for j in range(9):
            if row[j] != 1 or column[j] != 1:
                return False
    squares = collections.defaultdict(set)
    
    for i in range(9):
        for j in range(9):
            if board[i][j] in squares(i // 3, j // 3):
                return False
            squares(i // 3, j // 3).add(board[i][j])
    return True

board = [[0] * 9] * 9


for x in range(1, len(sys.argv)):
    group = sys.argv[x]
    board[int(sys.argv[x][0])][int(sys.argv[x][1])] = int(sys.argv[x][2])
    
    # run function 
    
    if is_correct(board) and is_complete(board):
        print('Sudoku successfully completed')
        exit
    print('You are stupid')
    


        