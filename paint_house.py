from typing import List


class Solution:
    def minCostDP(self, costs: List[List[int]]) -> int:
        """
        time: n
        space: 1
        """
        n = len(costs)
        if n == 0:
            return 0

        for i in range(len(costs) - 2, -1, -1):
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
            costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])

        return min(costs[0])

    def minCostDPBetter(self, costs: List[List[int]]) -> int:
        """
        time: n
        space: 1
        """
        n = len(costs)
        if n == 0:
            return 0

        prev_cost = costs[0][:]
        for i in range(1, n):
            curr_cost = costs[i][:]
            curr_cost[0] += min(prev_cost[1], prev_cost[2])
            curr_cost[1] += min(prev_cost[0], prev_cost[2])
            curr_cost[2] += min(prev_cost[0], prev_cost[1])
            prev_cost = curr_cost

        return min(prev_cost)


if __name__ == '__main__':
    s = Solution()
    assert s.minCostDP([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
    assert s.minCostDP([[7, 6, 2]]) == 2
