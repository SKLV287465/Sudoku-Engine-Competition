import helper as h
import src.main as m
import guess as g
import threading as th

def simple_solve(board):
    changes = 1
    while changes:
        changes = 0
        for x in range(9):
            for y in range(9):
                for n in range(1, 10):
                    if h.only_valid_in_box(n, x, y, board) or h.only_valid_in_col(n, x, y, board) or h.only_valid_in_row(n, x, y, board):
                        board[x][y] = n
                        changes += 1
    completed = False
    correct = False
    if m.is_complete(board):
        completed = True
    if m.is_correct(board):
        correct = True
    return board, completed, correct

def solve(board):
    board, done, solved = simple_solve(board)
    if solved and done: 
        return board
    binaries = g.get_binaries(board)
    correct_binary = [0] * len(binaries)
    for i in range(len(binaries)):
        new_board = board
        new_board[binaries[1]][binaries[2]] = binaries[0]
        
    return board