from typing import List


class Solution:
    """
    time: n * 2^n => 2^n recursions, with deep copy of nums (n) at each recursion
    space: n => stack at most has n recursions
    """
    def subsetsWithDupBacktrack(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        self.backtrack(nums, [], ans)
        return ans

    def backtrack(self, nums, path, ans):
        for i, v in enumerate(nums):
            if path[:] + [v] in ans:
                continue
            ans.append(path[:] + [v])
            self.backtrack(nums[i + 1:], path + [v], ans)