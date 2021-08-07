#!/usr/bin/env python
from print_matrix import print_matrix

def sort_matrix(matrix, rows, columns):
    print("Matrix before sort")
    print_matrix(matrix, rows, columns)
    temp = list()
    for row in range(0, rows):
        for col in range(0, columns):
            temp.append(matrix[row][col])

    temp.sort()
    n = 0
    for row in range(0, rows):
        for col in range(0, columns):
            matrix[row][col] = temp[n]
            n += 1

    print("Matrix after sort")
    print_matrix(matrix, rows, columns)
    return matrix


if __name__ == '__main__':
    mat = [[4, 6, 2],
           [1, 5, 7],
           [9, 3, 8]]
    mat2 = [[4, 6, 2, 7],
           [1, 5, 7, 6],
           [9, 3, 8, 8]]

    sort_matrix(mat2, 3, 4)
