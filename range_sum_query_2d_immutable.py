class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        time: r * c
        space: r * c
        """
        # r * c
        self.matrix = matrix[:]

        self.n_rows = len(self.matrix)  # r
        self.n_cols = len(self.matrix[0])  # c

        # r * c
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if 1 <= r < self.n_rows:
                    self.matrix[r][c] += self.matrix[r - 1][c]
                if 1 <= c < self.n_cols:
                    self.matrix[r][c] += self.matrix[r][c - 1]
                if 1 <= r < self.n_rows and 1 <= c < self.n_cols:
                    self.matrix[r][c] -= self.matrix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        time: 1
        space: 1
        """
        total = self.matrix[row2][col2]
        if 0 <= row1 - 1:
            total -= self.matrix[row1 - 1][col2]
        if 0 <= col1 - 1:
            total -= self.matrix[row2][col1 - 1]
        if 0 <= row1 - 1 and 0 <= col1 - 1:
            total += self.matrix[row1 - 1][col1 - 1]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)