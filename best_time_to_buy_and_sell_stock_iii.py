from typing import List


class Solution:
    """
    time: n
    space: 1
    """
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit



if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([3,3,5,0,0,3,1,4]) == 6
    # assert s.maxProfit([1,2,3,4,5]) == 4
    # assert s.maxProfit([7,6,4,3,1]) == 0
    # assert s.maxProfit([1]) == 0