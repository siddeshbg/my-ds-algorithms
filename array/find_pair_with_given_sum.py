"""
Problem URL: https://www.techiedelight.com/find-pair-with-given-sum-array/

Find pair with given sum in an array

Ex:
Input:

arr = [8, 7, 2, 5, 3, 1]
sum = 10

Output:

Pair found at index 0 and 2 (8 + 2)

or

Pair found at index 1 and 4 (7 + 3)
"""
# def find_pair(arr, sum):
#     pairs = list()
#     for i, x in enumerate(arr):
#         print("%d:%d" % (i, x))
#         for j, y in enumerate(arr[1:]):
#             print("\t%d:%d" % (j+1, y))
#             if (x+y) == sum:
#                 print("%d + %d = %d" % (x, y, sum))
#                 pairs.append((i, j+1))
#
#     return pairs


def find_pairs(arr, sum):
    pairs = list()
    for i, x in enumerate(arr):
        print("i->%d:%d" % (i, x))
        for j, y in enumerate(arr[i+1:]):
            print("\tj->%d:%d" % (j, y))
            if (x+y) == sum:
                print("%d + %d = %d" % (x, y, sum))
                pairs.append((x, y))

    return pairs


if __name__ == '__main__':
    arr = [8, 7, 2, 5, 3, 1]
    sum = 10
    pairs = find_pairs(arr, sum)
    for x, y in pairs:
        print("Pair found at index %d and %d (%d + %d)" %
              (arr.index(x), arr.index(y), x, y))
