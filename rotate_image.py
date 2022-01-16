from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.

    do for i/2 iterations, for offset in range(0, i/2)
    0,0 -> 0,j      0,1   -> 1,1
    0,j -> i,j      1,j-1 -> i,j-1
    i,j -> i,0      i,j-1 -> i-1,0
    i,0 -> 0,0      i-1,0 -> 0,1

    time: len(m) ^ 2
    space: 1
    """
    n = len(matrix)

    l, r = 0, n - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            tmp = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = tmp

        l += 1
        r -= 1

    """
    transpose + reverse rows
    0,j -> i,0
    0,1 -> 1,0
    1,3 -> 3,1
    time: 2 * (len(m) ^ 2)
    space: 1
    """
    n = len(matrix)

    # transpose
    for i in range(n):
        for j in range(i + 1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse rows
    for i in range(n):
        for j in range(n / 2):
            matrix[i][j]


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(a)
    print(a)
