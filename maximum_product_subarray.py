from typing import List


class Solution:
    """
    time: n
    space; 1
    """

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        cur_min, cur_max = nums[0], nums[0]
        ans = cur_max

        for i in range(1, n):
            cur_min, cur_max = min(nums[i], cur_min * nums[i], cur_max * nums[i]), \
                               max(nums[i], cur_min * nums[i], cur_max * nums[i])
            ans = max(ans, cur_max)

        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([0, 2]) == 2
    assert s.maxProduct([-2, 3, -4]) == 24
