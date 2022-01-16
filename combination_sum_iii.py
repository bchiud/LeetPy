from typing import List


class Solution:
    """
    time: 9! / ((9 - k)!) => permutation formula because it's an ordered combination
    space: k steps required
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        ans = []
        self.backtrack(nums, [], k, n, ans)
        return ans

    def backtrack(self, nums, path, k, n, ans):
        if len(path) == k and n == 0:
            ans.append(path)
        elif len(path) > k or n < 0:
            return
        else:
            for i in range(len(nums)):
                self.backtrack(nums[i + 1:], path + [nums[i]], k, n - nums[i], ans)


if __name__ == '__main__':
    s = Solution()
    assert s.combinationSum3(3, 7) == [[1, 2, 4]]
    assert s.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert s.combinationSum3(4, 1) == []
    assert s.combinationSum3(3, 2) == []
    assert s.combinationSum3(9, 45) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
