from typing import List


class Solution:
    def robDp(self, nums: List[int]) -> int:
        """
        time: n
        space: n
        """
        n = len(nums)

        if n == 0:
            return 0

        dp = [0] * (n + 1)
        dp[n - 1], dp[n] = nums[n - 1], 0

        for i in range(n - 2, -1, -1):
            # skip robbing current vs rob current and next next house
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]


    def robDpConstantSpace(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        next_next = 0
        next = nums[n - 1]

        for i in range(n - 2, -1, -1):
            next, next_next = max(nums[i] + next_next, next), next

        return next

if __name__ == '__main__':
    s = Solution()

    s.robDp([1,2,3,1]) == 4
    s.robDp([2,7,9,3,1]) == 12

    s.robDpConstantSpace([1,2,3,1]) == 4
    s.robDpConstantSpace([2,7,9,3,1]) == 12