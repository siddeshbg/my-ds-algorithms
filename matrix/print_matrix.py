#!/usr/bin/env python

def print_matrix(matrix, rows, columns):
    print("-" * 10)
    for i in range(0, rows):
        for j in range(0, columns):
            print(matrix[i][j], end=" ")
        print()
    print("-" * 10)

if __name__ == '__main__':
    matrix = [[5, 4, 7],
              [1, 3, 8],
              [2, 9, 6]]

    matrix = [[5, 4, 7, 7],
              [1, 3, 8, 8],
              [2, 9, 6, 6]]
    print_matrix(matrix, 3, 4)
