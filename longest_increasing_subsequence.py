from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLISDp(self, nums: List[int]) -> int:
        """
        time: n^2
        space: n
        """
        dp = [1] * (len(nums) + 1)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLISDpBinarySearch(self, nums: List[int]) -> int:
        """
        time: n log n
        space: n
        """
        sub = []  # subsequence
        for num in nums:
            i = bisect_left(sub, num)  # returns insertion point

            # num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # else replace first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)


if __name__ == '__main__':
    s = Solution()

    # assert s.lengthOfLISDp([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    # assert s.lengthOfLISDp([0, 1, 0, 3, 2, 3]) == 4
    # assert s.lengthOfLISDp([7, 7, 7, 7, 7, 7, 7]) == 1

    # assert s.lengthOfLISDpBinarySearch([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert s.lengthOfLISDpBinarySearch([0, 1, 0, 3, 2, 3]) == 4
    # assert s.lengthOfLISDpBinarySearch([7, 7, 7, 7, 7, 7, 7]) == 1
