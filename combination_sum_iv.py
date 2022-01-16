from typing import List


class Solution:
    """
    time: n! / (n! * (n - r)!)
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num <= i: dp[i] += dp[i-num]
                print(dp)
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    # assert s.combinationSum4([1, 2, 3], 4) == 7
    assert s.combinationSum4([9], 3) == 0
    # s.combinationSum4([4,2,1], 32)
