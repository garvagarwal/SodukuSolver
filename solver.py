#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Garv Agarwal"
__version__ = "0.1.0"
__license__ = "MIT"

# Imports
from math import sqrt


def solve():
    """ Main entry point of the app """
    print(valid_board([[1]], 1))


def valid_board(puzzle, size):
	numbers = set(range(1, size + 1))

	if len(puzzle) != size:						# Col sizes
		return False

	for i in range(size):
		col = set()

		for j in range(size):
			col.add(puzzle[j][i])
		
		if col != numbers:						# Col duplicates
			return False

	for row in puzzle:
		if len(row) != size:					# Row sizes
			return False
	
	for i in range(size):
		row = puzzle[i]

		if set(row) != numbers:					# Row duplicates
			return False


	for b in range(size):
		if not valid_box(puzzle, size, b):		# Boxes are good (correct sizes are implied from earlier checks)
			return False

	return True

def valid_box(puzzle, size, b):
	numbers = set(range(1, size + 1))
	vals = set()
	dim = int(sqrt(size))

	h = (b % 3) * dim
	v = (b // 3) * dim

	for r in range(dim):
		for c in range(dim):
			vals.add(puzzle[v+r][h+c])

	return vals == numbers


if __name__ == "__main__":
    """ This is executed when run from the command line """
    solve()
