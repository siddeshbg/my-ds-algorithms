#!/usr/bin/env python
"""
Print the large number and it's positions in the matrix
Input: [[7, 2, 4, 9],
        [4, 1, 6, 9],
        [7, 8, 1, 8]]
Output: The largest number in the matrix: is: 9 at position(s): [[0, 3], [1, 3]]
"""
import sys
from print_matrix import print_matrix


def get_large_number_in_matrix(matrix, rows, cols):
    max = -sys.maxsize - 1
    positions = list()
    for row in range(0, rows):
        for col in range(0, cols):
            if matrix[row][col] > max:
                max = matrix[row][col]
                positions = list()
                positions.append([row, col])
            elif matrix[row][col] == max:
                positions.append([row, col])

    print("The largest number in the matrix:")
    print_matrix(matrix, rows, cols)
    print("is: %s at position(s): %s" % (max, positions))
    return max


if __name__ == '__main__':
    mat = [[-7, -2, -4, -9],
           [-4, -1, -6, -9],
           [-7, -8, -1, -8]]

    mat2 = [[7, 2, 4, 9],
            [4, 1, 6, 9],
            [7, 8, 1, 8]]
    get_large_number_in_matrix(mat2, 3, 4)
