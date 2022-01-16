from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return nums[0]

        l, r = 0, n - 1

        while l < r:
            m = l + (r - l) // 2

            """
            use r because:
            1) increasing left side does not determine if lowest is on left side or ride side
            2) l will eventually converge with m 
            """
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        return nums[l]


if __name__ == '__main__':
    s = Solution()
    assert s.findMin([3,4,5,1,2]) == 1
    assert s.findMin([4,5,6,7,0,1,2]) == 0
    assert s.findMin([11,13,15,17]) == 11
    assert s.findMin([4,5,6,7,0,1,2]) == 0