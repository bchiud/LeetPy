import collections
from typing import List


class Solution:
    """
    k = max length of str
    time: n * (k log k)
    space: n * k
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stor = collections.defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            stor[key].append(s)

        ans = []
        for a in stor.values():
            ans.append(a)

        return ans

    """
    k = max length of str
    time: n * k
    space: n * k
    """

    def groupAnagramsFaster(self, strs: List[str]) -> List[List[str]]:
        words = collections.defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            words[tuple(chars)].append(s)

        return list(words.values())


if __name__ == '__main__':
    s = Solution()
    assert s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'],
                                                                           ['bat']]
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]

    assert s.groupAnagramsFaster(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'],
                                                                                 ['bat']]
    assert s.groupAnagramsFaster([""]) == [[""]]
    assert s.groupAnagramsFaster(["a"]) == [["a"]]
