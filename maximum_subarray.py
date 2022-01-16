from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        time: n
        space: 1
        """
        curr_sum, ans = nums[0], nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            ans = max(ans, curr_sum)

        print(ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([-1]) == -1
