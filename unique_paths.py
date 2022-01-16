class Solution:
    def uniquePathsBrute(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePathsBrute(m - 1, n) + self.uniquePathsBrute(m, n - 1);

    def uniquePathsDP(self, m: int, n: int) -> int:
        """
        time: m * n
        space: m * n
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def uniquePathsDPLessMemory(self, m: int, n: int) -> int:
        """
        time: m * n
        space: n
        """
        dp = [1 for _ in range(n)]
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.uniquePathsBrute(3, 7) == 28
    s.uniquePathsBrute(3, 2) == 3
    s.uniquePathsBrute(7, 3) == 28
    s.uniquePathsBrute(3, 3) == 6

    s.uniquePathsDP(3, 7) == 28
    s.uniquePathsDP(3, 2) == 3
    s.uniquePathsDP(7, 3) == 28
    s.uniquePathsDP(3, 3) == 6

    s.uniquePathsDPLessMemory(3, 7) == 28
    s.uniquePathsDPLessMemory(3, 2) == 3
    s.uniquePathsDPLessMemory(7, 3) == 28
    s.uniquePathsDPLessMemory(3, 3) == 6
