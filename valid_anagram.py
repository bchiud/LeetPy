class Solution:
    """
    time: n^2
    space: 1
    """

    def isAnagramSquared(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                i = t.find(c)
                t = t[:i] + '_' + t[(i + 1):]
            else:
                return False

        for c in t:
            if c != '_':
                return False
        return True

    """
    time: n
    space: 1
    """
    def isAnagramDict(self, s: str, t: str) -> bool:
        chars = {}

        for c in s:
            chars[c] = chars.get(c, 0) + 1

        for c in t:
            if c in chars:
                chars[c] -= 1
                if chars[c] == 0:
                    chars.pop(c)
            else:
                return False

        return len(chars) == 0

    """
    time: n
    space: 1
    """
    def isAnagramHashtable(self, s: str, t: str) -> bool:
        chars = [0] * 26

        for c in s:
            i = ord(c) - ord('a')
            chars[i] += 1

        for c in t:
            i = ord(c) - ord('a')
            chars[i] -= 1

        for i in chars:
            if i != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isAnagramSquared("anagram", "nagaram") is True
    assert s.isAnagramSquared("rat", "car") is False
    assert s.isAnagramSquared("ab", "a") is False

    assert s.isAnagramHashtable("anagram", "nagaram") is True
    assert s.isAnagramHashtable("rat", "car") is False
    assert s.isAnagramHashtable("ab", "a") is False

    assert s.isAnagramDict("anagram", "nagaram") is True
    assert s.isAnagramDict("rat", "car") is False
    assert s.isAnagramDict("ab", "a") is False
