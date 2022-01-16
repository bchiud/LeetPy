x   from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)

        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    assert s.coinChange([1,2,5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    assert s.coinChange([1], 1) == 1