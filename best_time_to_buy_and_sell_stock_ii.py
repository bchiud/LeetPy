from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        profit = 0
        for i in range(1, n):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit


if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 7
    assert s.maxProfit([1,2,3,4,5]) == 4
    assert s.maxProfit([7,6,4,3,1]) == 0