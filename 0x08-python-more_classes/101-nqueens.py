#!/usr/bin/python3
"""This module implements the N queen challenge"""
import sys


def is_safe(board, row, col, n):
    """returns boolean"""
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve_nqueens(board, col, n):
    """returns solutions"""
    if col == n:
        print(board)
        return True
    found_solution = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            found_solution = solve_nqueens(board, col + 1, n) or found_solution
            board[i][col] = 0
    return found_solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for x in range(n)] for y in range(n)]
    solve_nqueens(board, 0, n)
