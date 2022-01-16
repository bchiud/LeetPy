from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        time: n
        space: 1
        """
        i, n = 0, len(intervals)
        ans = []

        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        ans.append(newInterval)
        while i < n and intervals[i][0] <= ans[-1][1]:
            ans[-1][0] = min(ans[-1][0], intervals[i][0])
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
            i += 1

        while i < n and newInterval[1] < intervals[i][0]:
            ans.append(intervals[i])
            i += 1

        return ans

        # s, e = newInterval[0], newInterval[1]
        # left = [i for i in intervals if i[1] < s]
        # right = [i for i in intervals if i[0] > e]
        # if left + right != intervals:
        #     s = min(s, intervals[len(left)][0])
        #     e = max(e, intervals[-len(right) - 1][1])
        # return left + [[s, e]] + right

        # s, e = newInterval[0], newInterval[1]
        # left, right = [], []
        # for i in intervals:
        #     if i[1] < s:
        #         left += i,
        #     elif i[0] > e:
        #         right += i,
        #     else:
        #         s = min(s, i[0])
        #         e = max(e, i[1])
        # return left + [[s, e]] + right


if __name__ == '__main__':
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([], [5, 7]) == [[5, 7]]
    assert s.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert s.insert([[1, 5]], [2, 7]) == [[1, 7]]
    assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert s.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]
