class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        set_first_col_zero = False
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if col == 0:
                        set_first_col_zero = True
                    else:
                        matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(1, n):
                matrix[0][col] = 0

        if set_first_col_zero:
            for row in range(m):
                matrix[row][0] = 0
