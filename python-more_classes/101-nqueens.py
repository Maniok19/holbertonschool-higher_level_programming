#!/usr/bin/python3
"""N queens puzzle solver"""

import sys


def printSolution(board, size):
    """Print the solution in the required format"""
    solution = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def isSafe(board, row, col, size):
    """Check if a queen can be placed on board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, size):
    """Utility function to solve N Queen Problem"""
    if col >= size:
        return True

    for i in range(size):
        if isSafe(board, i, col, size):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, size):
                return True
            board[i][col] = 0

    return False


def solveNQ(size):
    """Initialize the board and solve the N Queen Problem"""
    board = [[0 for x in range(size)] for y in range(size)]

    if solveNQUtil(board, 0, size) is False:
        print("Solution does not exist")
        return False

    printSolution(board, size)
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQ(size)
