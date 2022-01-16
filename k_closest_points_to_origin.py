from math import sqrt
from typing import List

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """"
        time: n log k
        space: k
        """
        heap = []

        for x, y in points:
            # negate distance to create max heap
            dist = -(x**2 + y**2)

            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [[x, y] for dist, x, y in heap]
