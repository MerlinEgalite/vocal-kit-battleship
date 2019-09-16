#!/usr/bin/env python3

import numpy as np
from grid_init import generate_random_grid_and_boats, tuple_to_position, position_to_tuple


def affiche_simple_grille(grid):
    print(" ", end=" ")
    for i in range(9):
        print(i+1, end=" ")
    print(10)
    for i in range(10):
        print(chr(i+65), end=" ")
        for j in range(10):
            if grid[i][j] == "Water":
                print("-", end=" ")
            elif grid[i][j] == "Touched":
                print("T", end=" ")
            elif grid[i][j] == "Missed":
                print("W", end=" ")
            elif grid[i][j] == "Sunk":
                print("S", end=" ")
            else:
                print("-", end=" ")
        print("")

