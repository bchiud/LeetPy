import re
from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        return self.backtrack([sorted(s.split(',')) for s in re.split('{|}', s)])

    def backtrack(self, nodes) -> List[str]:
        if not nodes:
            return []
        if len(nodes) == 1:
            return nodes[0]

        paths = []
        options = nodes[0]
        for option in options:
            for path in self.backtrack(nodes[1:]):
                paths.append(option + path)
        return paths


if __name__ == '__main__':
    s = Solution()
    assert s.expand("{a,b}c{d,e}f") == ["acdf", "acef", "bcdf", "bcef"]
    # assert s.expand("abcd") == ["abcd"]
