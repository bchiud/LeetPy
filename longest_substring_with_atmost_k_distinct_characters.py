class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or k == 0:
            return 0

        sub_chars = defaultdict(int)

        l, r = 0, 0
        longest = 0

        while r < n:
            c = s[r]
            sub_chars[c] += 1

            while l < r and len(sub_chars) > k:
                c_l = s[l]
                sub_chars[c_l] -= 1
                if sub_chars[c_l] == 0:
                    del sub_chars[c_l]
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest
