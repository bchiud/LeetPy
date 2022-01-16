from typing import List


class Solution:
    def jumpDp(self, nums: List[int]) -> int:
        """
        time: n^2
        space: n
        """
        n = len(nums)
        if n <= 1:
            return 0

        dp = [float('inf')] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            if nums[i] != 0:
                min_moves = min(dp[i + 1:i + nums[i] + 1])
                if min_moves != float('inf'):
                    dp[i] = (1 + min_moves)
            print(dp)

        return dp[0]

    def jumpDpConstantSpace(self, nums: List[int]) -> int:
        """
        time: n
        space: 1
        """
        if len(nums) <= 1:
            return 0

        jumps = left = right = 0
        while right < len(nums) - 1:

            curr_reachable = 0
            for i in range(left, right + 1):
                curr_reachable = max(curr_reachable, i + nums[i])

            left = right + 1  # start at next unassessed index
            right = curr_reachable
            jumps += 1

        return jumps


if __name__ == '__main__':
    s = Solution()

    assert s.jumpDp([2, 3, 1, 1, 4]) == 2
    assert s.jumpDp([2, 3, 0, 1, 4]) == 2

    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2
