from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        next, next_next = nums[n - 1], 0
        for i in range(n - 2, -1, -1):
            next, next_next = max(nums[i] + next_next, next), next

        return next
