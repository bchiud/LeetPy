from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.n_rows, self.n_cols = len(board), len(board[0])

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.explore(i, j, word):
                    return True

        return False

    def explore(self, i: int, j: int, s: str) -> bool:
        if len(s) == 0:
            return True

        if i < 0 or i >= self.n_rows or j < 0 or j >= self.n_cols or self.board[i][j] != s[0]:
            return False

        self.board[i][j] = '#'

        ans = self.explore(i - 1, j + 0, s[1:]) or self.explore(i + 1, j + 0, s[1:]) \
              or self.explore(i + 0, j - 1, s[1:]) or self.explore(i + 0, j + 1, s[1:])

        self.board[i][j] = s[0]
        return ans
