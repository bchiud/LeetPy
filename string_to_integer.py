class Solution:
    """
    time: n
    space: 1
    """
    def myAtoi(self, s: str) -> int:
        chars = list(s.strip())

        if len(chars) == 0:
            return 0

        sign = -1 if chars[0] == '-' else 1
        if chars[0] in ['+', '-']:
            del chars[0]

        ans, i = 0, 0
        while i < len(chars) and chars[i].isdigit():
            ans = ans * 10 + (ord(chars[i]) - ord('0'))
            i += 1

        return min(2**31 - 1, max(sign * ans, -2**31))

if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi("42") == 42
    assert s.myAtoi("   -42") == -42
    assert s.myAtoi("4193 with words") == 4193
    assert s.myAtoi("words and 987") == 0
    assert s.myAtoi("-91283472332") == -2147483648


