class Solution:
    def climbStairsRecursive(self, n: int) -> int:
        if n in [1,2]:
            return n
        return self.climbStairsRecursive(n - 1) + self.climbStairsRecursive(n - 2)

    def climbStairsDpBottomUp(self, n: int) -> int:
        """
        time: n
        space: n
        """
        if n <= 2:
            return n

        dp = [None] * (n + 1)
        for i in range(3):
            dp[i] = i

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairsDpBottomUpConstantSpace(self, n: int) -> int:
        """
        time: n
        space: 1
        """
        prev = curr = 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr

if __name__ == '__main__':
    s = Solution()

    assert s.climbStairsRecursive(1) == 1
    assert s.climbStairsRecursive(2) == 2
    assert s.climbStairsRecursive(3) == 3

    assert s.climbStairsDpBottomUp(1) == 1
    assert s.climbStairsDpBottomUp(2) == 2
    assert s.climbStairsDpBottomUp(3) == 3

    assert s.climbStairsDpBottomUpConstantSpace(1) == 1
    assert s.climbStairsDpBottomUpConstantSpace(2) == 2
    assert s.climbStairsDpBottomUpConstantSpace(3) == 3

