from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        time: n
        space: 1
        """
        if not matrix:
            return []

        r_start, r_end = 0, len(matrix) - 1
        c_start, c_end = 0, len(matrix[0]) - 1
        ans = []

        while r_start <= r_end and c_start <= c_end:
            for c in range(c_start, c_end + 1):
                ans.append(matrix[r_start][c])
            for r in range(r_start + 1, r_end + 1):
                ans.append(matrix[r][c_end])
            if r_start < r_end and c_start < c_end:
                for c in range(c_end - 1, c_start - 1, -1):
                    ans.append(matrix[r_end][c])
                for r in range(r_end - 1, r_start, -1):
                    ans.append(matrix[r][c_start])
            r_start += 1
            r_end -= 1
            c_start += 1
            c_end -= 1
            
        return ans

