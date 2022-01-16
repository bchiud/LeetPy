import operator
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isnumeric():
            return int(expression)

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }
        ans = set()
        for i, c in enumerate(expression):
            if c in '+-*':
                s = self.diffWaysToCompute(expression[:i]) + c + self.diffWaysToCompute(expression[i + 1:])
                ans.add(eval(s))

        return list(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute("2-1-1") )
    # assert s.diffWaysToCompute("2-1-1") == [0, 2]
    # assert s.diffWaysToCompute("2*3-4*5") == [-34, -14, -10, -10, 10]
