class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        time: n
        space: n
        """
        ans = list(s)
        open_parens_stack = []

        for i, c in enumerate(ans):
            if c == "(":
                open_parens_stack.append(i)
            elif c == ")":
                if open_parens_stack:
                    open_parens_stack.pop()
                else:
                    ans[i] = ''

        while open_parens_stack:
            i = open_parens_stack.pop()
            ans[i] = ''

        return ''.join(ans)