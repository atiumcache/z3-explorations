from z3 import *
import time


def print_queens_board(solution):
    """Prints a crude gameboard showing queen placement."""
    n = len(solution)
    
    # Create an empty board
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Place the queens on the board
    for col in range(n):
        row = solution[col]
        board[row][col] = 'Q'
    
    # Print the board
    for row in board:
        print(' '.join(row))


def solve_queens(n):
    """
    Solves the N queens problem. 
    https://en.wikipedia.org/wiki/Eight_queens_puzzle

    Args:
        n (Int): Number of queens, and the dimensions of the NxN gameboard.
    """    
    start_time = time.time()

    solver = Solver()

    # Generate integers that represent queen positions
    # queens[i] is in column i. 
    # The int value of queens[i] is its row. 
    queens = [Int(f'Q_{i+1}') for i in range(n)]

    # Each queen must be in a different row.
    # A queen can only be placed in rows 0 through n. 
    solver.add([And(queens[i] >= 0, queens[i] < n) for i in range(n)])

    # Each queen must be placed in a different column.
    solver.add(Distinct(queens))

    # Queens cannot be on the same diagonal.
    solver.add([If(i != j, And(queens[i] != queens[j], queens[i] - i != queens[j] - j, queens[i] + i != queens[j] + j), True) for i in range(n) for j in range(n)])

    # Check if a solution exists
    if solver.check() == sat:
        model = solver.model()
        solution = [model.evaluate(queens[i]).as_long() for i in range(n)]
        end_time = time.time()
        print(f"Solution for {n} Queens:")
        print_queens_board(solution)
        print('Time Elapsed:', end_time - start_time, 'seconds.\n')
    else:
        end_time = time.time()
        print(f"No solution exists for {n} Queens")
        print('Time Elapsed:', end_time - start_time, 'seconds.\n')

    









