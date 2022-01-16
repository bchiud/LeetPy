from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        """
        time: n
        space: n
        """
        self.v1 = v1
        self.v2 = v2
        self.index = 0
        v1_len, v2_len = len(v1), len(v2)
        self.longer = self.v1 if v1_len > v2_len else self.v2
        self.min_len = min(v1_len, v2_len)
        self.total_len = v1_len + v2_len

    def next(self) -> int:
        """
        time: 1
        space: 1
        """

        ans = -1

        if self.index < self.total_len:
            if self.index < self.min_len * 2:
                if self.index % 2 == 0:
                    ans = self.v1[self.index // 2]
                else:
                    ans = self.v2[self.index // 2]
            else:
                ans = self.longer[self.index - self.min_len]

        self.index += 1
        return ans

    def hasNext(self) -> bool:
        """
        time: 1
        space: 1
        """
        return self.index < self.total_len

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
