"""Task 3.

Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Check board, return who win or draw/unfinished."""
    a, b, c = board
    diag_1 = [a[0], a[1], a[2]]
    diag_2 = [a[2], b[1], c[0]]
    diags = [diag_1, diag_2]
    for rows in [board, zip(*board), diags]:
        for line in rows:
            if "-" not in line and len(set(line)) == 1:
                return f"{line[0]} wins!"
    if "-" in {char for line in board for char in line}:  # noqa : C412
        return "unfinished!"
    return "draw!"
