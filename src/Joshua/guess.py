import helper as h
# check that it is only valid in row
def double_valid_in_row(number, x, y, board):
    coords = []
    if not h.valid_box(number, x, y, board) or not h.valid_row(number, x, y, board):
        return False
    for i in range(9):
        if i == y:
            continue
        if h.valid_col(board[x][i]):
            coords.append[number]
            coords.append[x]
            coords.append[i]
            coords.append[x]
            coords.append[y]
    if (len(coords) != 5):
        return False
    return coords

# check that it is only valid in col
def double_valid_in_col(number, x, y, board):
    if not h.valid_box(number, x, y, board) or not h.valid_col(number, x, y, board):
        return False
    coords = []
    for i in range(9):
        if i == x:
            continue
        if h.valid_row(board[i][y]):
            coords.append[number]
            coords.append[i]
            coords.append[y]
            coords.append[x]
            coords.append[y]
    if len(coords) != 5:
        return False
    return coords

# check that it is only valid in box
def double_valid_in_box(number, x, y, board):
    coords = []
    if not h.valid_box(number, x, y, board):
        return False
    bx = x // 3
    by = y // 3
    for i in range(3 * bx, 3 * bx + 3):
        for j in range(3 * by, 3 * by + 3):
            if y == j and x == i:
                continue
            if h.valid_col(board[i][j]) and h.valid_row(board[i][j]):
                coords.append[number]
                coords.append(i)
                coords.append(j)
                coords.append[x]
                coords.append[y]
    if len(coords) != 5:
        return False
    return coords



# find cases when we could guess between two choices
def get_binaries(board):
    # tuple of number, x_1, y_1, x_2, y_2 in a list
    binaries = []
    
    for number in range(1, 10):
        for x in range(9):
            for y in range(9):
                if double_valid_in_row(number, x, y, board):
                    binaries.append(double_valid_in_row(number, x, y, board))
                if double_valid_in_col(number, x, y, board):
                    binaries.append(double_valid_in_col(number, x, y, board))
                if double_valid_in_box(number, x, y, board):
                    binaries.append(double_valid_in_box(number, x, y, board))
    return binaries
    # get row binaries
    # get column binaries
    # get box binaries