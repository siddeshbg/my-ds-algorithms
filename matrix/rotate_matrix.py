#!/usr/bin/env python
"""
Given a matrix, clockwise rotate elements in it.

Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

"""
from print_matrix import print_matrix


def rotate_matrix(matrix, rows, columns):
    print_matrix(matrix, rows, columns)
    top = matrix[0][0]
    bottom = matrix[0][len(matrix)-1]
    left =


if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    # print(len(mat[0]))
    # rotate_matrix(mat, 3, 3)

    for i in range(2, -1, -1):
        print(i)

