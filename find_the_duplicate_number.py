from typing import List


class Solution:
    def findDuplicateNegativeMarking(self, nums: List[int]) -> int:
        """
        time: n
        space: 1
        """
        for n in nums:
            if nums[abs(n)] > 0:
                nums[abs(n)] *= -1
            else:
                return abs(n)

    def findDuplicateFloydHareAndTortoise(self, nums: List[int]) -> int:
        """
        time: n
        space: 1
        """
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast