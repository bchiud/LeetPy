from typing import List


class Solution:
    def combineBacktrack(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                ans.append(curr[:])
            else:
                for i in range(first, n + 1):
                    curr.append(i)
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack()
        return ans

    def combineDfs(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i for i in range(1, n + 1)]
        self.dfs(nums, [], ans, k)
        return ans

    def dfs(self, nums, path, ans, k):
        if len(path) == k:
            ans.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[i + 1:], path + [nums[i]], ans, k)


if __name__ == '__main__':
    s = Solution()

    assert s.combineBacktrack(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert s.combineBacktrack(1, 1) == [[1]]

    assert s.combineDfs(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert s.combineDfs(1, 1) == [[1]]
