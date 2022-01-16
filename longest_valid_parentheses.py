class Solution:
    """
    time: n
    space: n
    """
    def longestValidParenthesesStack(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans

    """
    time: n
    space: n
    """
    def longestValidParentheses(self, s: str) -> int:
        ans = 0

        l = r = 0
        for c in s:
            if c == "(":
                l += 1
            else:
                r += 1

            if l == r:
                ans = max(ans, l + r)
            elif l < r:
                l = r = 0

        l = r = 0
        for c in s[::-1]:
            if c == "(":
                l += 1
            else:
                r += 1

            if l == r:
                ans = max(ans, l + r)
            elif l > r:
                l = r = 0

        return ans

if __name__ == '__main__':
    s = Solution()
    assert s.longestValidParenthesesStack("(()") == 2
    assert s.longestValidParenthesesStack(")()())") == 4
    assert s.longestValidParenthesesStack("()") == 2
    assert s.longestValidParenthesesStack("") == 0