class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        time: n
        space: 1
        """
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        ans = [''] * numRows
        row, step = 0, 1
        for c in s:
            ans[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return ''.join(ans)
