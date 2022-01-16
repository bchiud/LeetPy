class Solution:
    """
    time: n^2
    space: 1
    """

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s or n < 2:
            return s

        ans = ""
        for i in range(n):
            tmp = self.helper(s, i, i)
            if len(ans) < len(tmp):
                ans = tmp
            tmp = self.helper(s, i, i + 1)
            if len(ans) < len(tmp):
                ans = tmp

        return ans

    def helper(self, s: str, left: int, right: int) -> str:
        n = len(s)
        while 0 <= left and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def longestPalindromeDP(self, s: str) -> str:
        """
        time: n^2
        space: n^2
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = ''

        # all single chars are palindromes
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        # start from back since l + 1 is required to determine inner string
        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    if r - l == 1 or dp[l + 1][r - 1]:  # two chars, or remaining str inside is palindrome
                        dp[l][r] = True
                        if len(ans) < (r - l + 1):
                            ans = s[l:(r + 1)]

        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.longestPalindromeDP("babad") == "aba" or s.longestPalindromeDP("babad") == "bab"
    assert s.longestPalindromeDP("cbbd") == "bb"
    assert s.longestPalindromeDP("a") == "a"
    assert s.longestPalindromeDP("ac") == "a" or s.longestPalindromeDP("ac") == "c"
    assert s.longestPalindromeDP("aacabdkacaa") == "aca"
