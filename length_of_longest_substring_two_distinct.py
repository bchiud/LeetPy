class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r = 0, 0
        chars = {}
        ans = None, None  # l, r

        while r < len(s):
            # print(f'L: {l}, R: {r}')
            chars[s[r]] = chars.get(s[r], 0) + 1

            while len(chars) > 2 and l < r:
                chars[s[l]] = chars[s[l]] - 1
                if chars[s[l]] == 0:
                    del chars[s[l]]

                l += 1

            if ans[0] is None or r - l > ans[1] - ans[0]:
                ans = l, r

            r += 1

        # print(0 if ans[0] is None else (ans[1] - ans[0] + 1))
        return 0 if ans[0] is None else (ans[1] - ans[0] + 1)

if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstringTwoDistinct("eceba") == 3
    assert s.lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5
    assert s.lengthOfLongestSubstringTwoDistinct("a") == 1