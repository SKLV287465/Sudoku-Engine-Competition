import helper as h

def solve(board):
    changes = 1
    while changes:
        changes = 0
        for x in range(9):
            for y in range(9):
                for n in range(1, 10):
                    if h.only_valid_in_box(n, x, y, board) or h.only_valid_in_col(n, x, y, board) or h.only_valid_in_row(n, x, y, board):
                        board[x][y] = n
                        changes += 1
    return board