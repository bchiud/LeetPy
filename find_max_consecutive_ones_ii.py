from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        time: n
        space: 1
        """
        n = len(nums)

        if n <= 1:
            return 1

        l, r = 0, 0
        max_consecutive = 0
        zeroes = 0

        while r < n:
            if nums[r] == 0:
                zeroes += 1

            while zeroes == 2:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            max_consecutive = max(max_consecutive, r - l + 1)
            r += 1

        return max_consecutive

if __name__ == '__main__':
    s = Solution()
    assert s.findMaxConsecutiveOnes([1,0,1,1,0]) == 4
    assert s.findMaxConsecutiveOnes([1,0,1,1,0,1]) == 4




