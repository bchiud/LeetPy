from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtracking(candidates, [], target, ans)
        return ans

    def backtracking(self, candidates, path, target, ans):
        if target < 0:
            return
        elif target == 0:
            ans.append(path)
        else:
            for i in range(len(candidates)):
                if i > 0 and candidates[i - 1] == candidates[i]:
                    continue
                else:
                    self.backtracking(candidates[i + 1:], path + [candidates[i]], target - candidates[i], ans)


if __name__ == '__main__':
    s = Solution()

    assert s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
    assert s.combinationSum2([2,5,2,1,2], 5) == [
        [1,2,2],
        [5]
    ]
