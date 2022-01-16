class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, c in enumerate(s):
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                open = stack.pop()
                if (open != "(" and c == ")") or (open != "[" and c == "]") or (open != "{" and c == "}"):
                    return False

        return len(stack) == 0

if __name__ == '__main__':
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True
