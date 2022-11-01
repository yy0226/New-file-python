#!/usr/bin/env python
# coding: utf-8

from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point->22
        y (int): Y-coordinate of the flood start point->8
    Returns:
        List[str]: Modified board
    """
    len_x = len(input_board)
    len_y = len(input_board[0])
    if x < 0 or x >= len_x:
        return
    if y < 0 or y >= len_y:
        return
    if input_board[x][y] == "#" or input_board[x][y] == new: return
    if input_board[x][y] == ".":
        input_board[x]=input_board[x][0:y]+ new +input_board[x][y+1:]
  
    flood_fill(input_board, old, new, x-1, y)
    flood_fill(input_board, old, new, x+1, y)
    flood_fill(input_board, old, new, x, y-1)
    flood_fill(input_board, old, new, x, y+1)
    
    return input_board


# Expected output:)):
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

modified_board = flood_fill(input_board = board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

