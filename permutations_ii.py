from typing import List


class Solution:
    def permuteUniqueBacktrack(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []

        def backtrack(first, curr=[]):
            if len(curr) == n:
                ans.append(curr)


    def permuteUniqueDfs(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, path, ans):
        if not nums:
            ans.append(path)
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                else:
                    self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], ans)


if __name__ == '__main__':
    s = Solution()
    assert s.permuteUniqueDfs([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert s.permuteUniqueDfs([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
