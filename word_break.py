from collections import deque
from functools import lru_cache
from typing import List, Set, FrozenSet


class Solution:
    def wordBreakBrute(self, s: str, wordDict: List[str]) -> bool:
        """
        time: 2^n
        space: 2^n
        """
        def wordBreakRecur(s: str, word_dict: Set[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)

    def wordBreakRecursionWithMemo(self, s: str, wordDict: List[str]) -> bool:
        """
        time: n^3
        space: n
        """
        @lru_cache
        def wordBreakMemo(s: str, word_dict: FrozenSet[str], start: int) -> bool:
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False

        return wordBreakMemo(s, frozenset(wordDict), 0)

    def wordBreakBfs(self, s: str, wordDict: List[str]) -> bool:
        """
        time: n^3
        space: n
        """
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
                visited.add(start)
        return False

    def wordBreakDp(self, s: str, wordDict: List[str]) -> bool:
        """
        time: n^3
        space: n
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

if __name__ == '__main__':
    s = Solution()
    assert s.wordBreakBrute("leetcode", ["leet","code"]) == True
    assert s.wordBreakBrute("applepenapple", ["apple","pen"]) == True
    assert s.wordBreakBrute("catsandog", ["cats","dog","sand","and","cat"]) == False

    assert s.wordBreakRecursionWithMemo("leetcode", ["leet","code"]) == True
    assert s.wordBreakRecursionWithMemo("applepenapple", ["apple","pen"]) == True
    assert s.wordBreakRecursionWithMemo("catsandog", ["cats","dog","sand","and","cat"]) == False

    assert s.wordBreakBfs("leetcode", ["leet","code"]) == True
    assert s.wordBreakBfs("applepenapple", ["apple","pen"]) == True
    assert s.wordBreakBfs ("catsandog", ["cats","dog","sand","and","cat"]) == False

    assert s.wordBreakDp("leetcode", ["leet","code"]) == True
    assert s.wordBreakDp("applepenapple", ["apple","pen"]) == True
    assert s.wordBreakDp("catsandog", ["cats","dog","sand","and","cat"]) == False