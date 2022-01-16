import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        n, m = len(s), len(t)
        if n < m:
            return ""

        ans_l, ans_r = float('-inf'), float('inf')

        required_chars = collections.Counter(t)
        required_uniques = len(required_chars)

        l_i = 0
        for r_i, r_char in enumerate(s):
            if r_char in required_chars.keys():
                required_chars[r_char] -= 1
                if required_chars[r_char] == 0:
                    required_uniques -= 1

            # contract
            while required_uniques == 0:
                if (ans_r - ans_l) > (r_i - l_i):
                    ans_l, ans_r = l_i, r_i

                l_char = s[l_i]
                if l_char in required_chars.keys():
                    if required_chars[l_char] == 0:
                        required_uniques += 1
                    required_chars[l_char] += 1
                l_i += 1

        return s[ans_l : (ans_r + 1)] if ans_r != float('inf') else ""


if __name__ == '__main__':
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
