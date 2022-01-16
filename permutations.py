from typing import List


class Solution:
    def permuteBacktrack(self, nums):
        """
        time: ~ n * n!
        space: ~ n * n! -> # of recursions
        """
        n = len(nums)
        ans = []

        def backtrack(first=0):
            if first == n:
                ans.append(nums[:])
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first]


        backtrack()
        return ans

    def permuteDfs(self, nums: List[int]) -> List[List[int]]:
        """
        time: n * n! => splice operation is n and will be done n! times
        space: n * n! => len(nums) + len(path) == n. done n! times
        """
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums: List[int], path, ans):
        if not nums:
            ans.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], ans)

if __name__ == '__main__':
    s = Solution()
    assert s.permuteBacktrack([1, 2, 3]) in [
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    ]

    assert s.permuteDfs([1, 2, 3]) in [
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    ]
