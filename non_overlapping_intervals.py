from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        time: n log n => sort
        space: 1
        """
        remove, end = 0, float('-inf')
        for s, e in sorted(intervals, lambda x: x[1]):
            if end <= s:
                end = e
            else:
                remove += 1
        return remove