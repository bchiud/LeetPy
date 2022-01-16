from typing import List


class Solution:
    """
    time: n
    space: 1
    """
    def maxProfit(self, prices: List[int]) -> int:
        # largest = prices[-1]
        # profit = 0
        #
        # n = len(prices)
        # for i in range(n - 2, -1, -1):
        #     profit = max(profit, largest - prices[i])
        #     largest = max(largest, prices[i])
        #
        # return profit

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit




if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
