from typing import List


class Solution:
    """
    backtracking
    time: n ^ m => worst case is target is built using all 1's
    space: m => worst case space complexity where recursion is called m times using all 1's
    """
    def combinationSumBacktracking(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.backtracker(candidates, target, [], ans)
        return ans

    def backtracker(self, candidates: List[int], target: int, path: List[int], ans: List[List[int]]):
        if target < 0:
            return
        elif target == 0:
            ans.append(path)
            return
        else:
            for i in range(len(candidates)):
                # candidates[i:] starts at i so we dont use any number less than current. this is to prevent dups
                self.backtracker(candidates[i:], target - candidates[i], path + [candidates[i]], ans)


    """
    dp
    time:
    space:
    """

    def combinationSumDP(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for c in candidates:  # O(N): for each candidate
            for i in range(c, target + 1):  # O(M): for each possible value <= target
                print(f'c: {c}, i: {i}')
                if i == c:
                    dp[i].append([c])

                for comb in dp[i - c]:
                    print(f'Before: {dp}')
                    dp[i].append(comb + [c])  # O(M) worst: for each combination
                    print(f'After : {dp}')
        print(f'ans: {dp[-1]}')
        return dp[-1]


if __name__ == '__main__':
    s = Solution()

    assert s.combinationSumBacktracking([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert s.combinationSumBacktracking([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSumBacktracking([2], 1) == []
    assert s.combinationSumBacktracking([1], 1) == [[1]]
    assert s.combinationSumBacktracking([1], 2) == [[1, 1]]

    assert s.combinationSumDP([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert s.combinationSumDP([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSumDP([2], 1) == []
    assert s.combinationSumDP([1], 1) == [[1]]
    assert s.combinationSumDP([1], 2) == [[1, 1]]
