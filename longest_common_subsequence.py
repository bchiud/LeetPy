class Solution:
    def longestCommonSubsequenceDp(self, text1: str, text2: str) -> int:
        """
        time: m * n
        space: m * n
        """
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for col in range(len(text2) - 1, -1, -1):
            for row in range(len(text1) - 1, -1, -1):
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]

    def longestCommonSubsequenceDpSpaceOptimized(self, text1: str, text2: str):
        # make sure text1 is shorter to conserve space
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        previous = [0] * (len(text1) + 1)

        for j in range(len(text2) - 1, -1, -1):
            current = [0] * (len(text1) + 1)
            for i in range(len(text1) - 1, -1, -1):
                if text1[i] == text2[j]:
                    current[i] = 1 + previous[i + 1]
                else:
                    current[i] = max(previous[i], current[i + 1])
            previous = current

        return previous[0]


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonSubsequenceDp("abcde", "ace") == 3
    assert s.longestCommonSubsequenceDp("abc", "abc") == 3
    assert s.longestCommonSubsequenceDp("abc", "def") == 0

    assert s.longestCommonSubsequenceDpSpaceOptimized("abcde", "ace") == 3
    assert s.longestCommonSubsequenceDpSpaceOptimized("abc", "abc") == 3
    assert s.longestCommonSubsequenceDpSpaceOptimized("abc", "def") == 0
