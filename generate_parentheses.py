from typing import List


class Solution:
    def generateParenthesisBacktracking(self, n: int) -> List[str]:
        ans = []

        def backtracking(s: str, left: int, right: int) -> None:
            if len(s) == n * 2:
                ans.append(s)
            if left < n:
                backtracking(s + '(', left + 1, right)
            if right < left:
                backtracking(s + ')', left, right + 1)

        backtracking("", 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.generateParenthesisBacktracking(1) == ["()"]
    assert s.generateParenthesisBacktracking(2) == ['(())', '()()']
