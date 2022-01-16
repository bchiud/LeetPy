from typing import List


class Solution:
    """
    1. each leg must result in tank > 0, else start at next station
    2. if total cost > total gas, circuit is impossible
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        total_tank, current_tank, starting_station = 0, 0, 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                starting_station = i + 1
                current_tank = 0

        return starting_station if total_tank >= 0 else -1


if __name__ == '__main__':
    s = Solution()