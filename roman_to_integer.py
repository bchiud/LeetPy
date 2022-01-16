class Solution:
    def romanToInt(self, s: str) -> int:
        """
        time: n
        space: 1
        """
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        i, n, ans = 0, len(s), 0
        while i < n:
            if i + 1 < n and map[s[i]] < map[s[i + 1]]:
                ans += (map[s[i + 1]] - map[s[i]])
                i += 2
            else:
                ans += map[s[i]]
                i += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
