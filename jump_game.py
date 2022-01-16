from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        left_most_good_index = n - 1
        for i in range(n - 1, -1, -1):
            if left_most_good_index <= i + nums[i]:
                left_most_good_index = i

        return left_most_good_index == 0

if __name__ == '__main__':
    s = Solution()
    assert s.canJump([2,3,1,1,4]) == True
    assert s.canJump([3,2,1,0,4]) == False

