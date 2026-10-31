"""Assignment 4: N-Queens Constraint Satisfaction Problem"""

CODE = '''def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1
    return False

def print_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

n = 5
board = [-1] * n
if solve_n_queens(board, 0, n):
    print("\\nSolution:")
    print_board(board, n)
else:
    print("No solution exists.")

# Output (n=5)
# Solution:
# Q . . . .
# . . Q . .
# . . . . Q
# . Q . . .
# . . . Q .
'''

def nqueens():
    """
    Assignment 4 - N-Queens Constraint Satisfaction Problem (CSP)
    
    Prints the N-Queens solver using backtracking (CSP).
    Usage: heapplot.nqueens()
    """
    print(CODE)
