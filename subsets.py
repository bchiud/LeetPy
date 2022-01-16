from typing import List


class Solution:
    """
    time: n * (2^n)
    space: n * (2^n) => 2^n solutions of length n
    """
    def subsetsCasdaing(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for n in nums:
            ans += [curr + [n] for curr in ans]

        return ans

    def subsetsBacktracking(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans

    def backtrack(self, nums, path, ans):
        ans.append(path[:])
        for i, v in enumerate(nums):
            self.backtrack(nums[i + 1:], path + [v], ans)

