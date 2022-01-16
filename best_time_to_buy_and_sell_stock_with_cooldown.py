from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy, sell, rest = -prices[0], 0, 0

        for p in prices:
            """
            max profit of each state at each point in time:
            buy: must have rested the day before buying, so substract current price from rest
            sell: buy (includes cost of purchasing) + profit gained, aka current price
            rest: max is always sell since buy < rest < sell, since:
                1) buy is always reduced by cost of purchasing
                2) buy must come before sell
                3) rest can never be greater than sell (realizing a profit)
            """
            buy, sell, rest = max(buy, rest - p), max(sell, buy + p), sell

        return sell