from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        time: 1
        space: 1
        """
        self.lo = []
        self.hi = []

    def addNum(self, num):
        """
        time: log n
        space: n
        """
        heappush(self.lo, -num)             # lo is maxheap, so -1 * num
        heappush(self.hi, -self.lo[0])      # hi is minheap
        heappop(self.lo)

        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)

    def findMedian(self):
        """
        time: log n
        space: 1
        """
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()