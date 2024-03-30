
# check if the row is valid for the number
def valid_row(number, x, y, board):
    if board[x][y] != 0:
        return False
    for i in range(9):
        if board[x][i] == number:
            return False
    return True
    
# check if the column is valid for the number
def valid_col(number, x, y, board):
    if board[x][y] != 0:
        return False
    for i in range(9):
        if board[i][y] == number:
            return False
    return True
    
# check if the box is valid for the number
def valid_box(number, x, y, board):
    if board[x][y] != 0:
        return False
    bx = x // 3
    by = y // 3
    for i in range(3 * bx, 3 * bx + 3):
        for j in range(3 * by, 3 * by + 3):
            if board[i][j] == number:
                return False
    return True

# check that it is only valid in row
def only_valid_in_row(number, x, y, board):
    if not valid_box(number, x, y, board) or not valid_row(number, x, y, board):
        return False
    for i in range(9):
        if i == y:
            continue
        if valid_col(board[x][i]):
            return False
    return True
# check that it is only valid in col
def only_valid_in_col(number, x, y, board):
    if not valid_box(number, x, y, board) or not valid_col(number, x, y, board):
        return False
    for i in range(9):
        if i == x:
            continue
        if valid_row(board[i][y]):
            return False
    return True
# check that it is only valid in box
def only_valid_in_box(number, x, y, board):
    if not valid_box(number, x, y, board):
        return False
    bx = x // 3
    by = y // 3
    for i in range(3 * bx, 3 * bx + 3):
        for j in range(3 * by, 3 * by + 3):
            if y == j and x == i:
                continue
            if valid_col(board[i][j]) and valid_row(board[i][j]):
                return False
    return True