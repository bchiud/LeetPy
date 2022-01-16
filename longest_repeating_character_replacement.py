from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = max_freq = max_len = 0
        for right in range(len(s)):
            c = s[right]
            counts[c] += 1

            max_freq = max(max_freq, counts[c])

            # invalid substring: len of curr string less freq of curr char
            if ((right - left + 1) - max_freq) > k:
                counts[s[left]] -= 1
                left += 1
            else:
                max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == '__main__':
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
    assert s.characterReplacement("AABA", 0) == 2
    assert s.characterReplacement("ABAA", 0) == 2
    assert s.characterReplacement("BAAA", 0) == 3