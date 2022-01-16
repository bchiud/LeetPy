from typing import List


class Solution:
    def pacificAtlanticBfs(self, heights: List[List[int]]) -> List[List[int]]:
        """
        time: m * n
        space: m * n => worst case total queue space
        """
        m, n = len(heights), len(heights[0])

        pacific_queue = [(row, 0) for row in range(m)] + [(0, col) for col in range(1, n)]
        atlantic_queue = [(row, n - 1) for row in range(m)] + [(m - 1, col) for col in range(0, n - 1)]

        def bfs(queue):
            reachable = set()

            while queue:
                (a, b) = queue.pop(0)
                reachable.add((a, b))
                for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    x = a + x
                    y = b + y
                    if 0 <= x < m and 0 <= y < n \
                            and not (x, y) in reachable \
                            and heights[a][b] <= heights[x][y]:
                        queue.append((x, y))

            return reachable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        return list(pacific_reachable.intersection(atlantic_reachable))

    def pacificAtlanticDfs(self, heights: List[List[int]]) -> List[List[int]]:
        """
        time: m * n
        space: m * n => recursion space
        """
        m, n = len(heights), len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, reachable):
            reachable.add((row, col))
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x = row + x
                y = col + y
                if 0 <= x < m and 0 <= y < n \
                        and not (x, y) in reachable \
                        and heights[row][col] <= heights[x][y]:
                    dfs(x, y, reachable)

        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n - 1, atlantic_reachable)

        for j in range(n - 1):
            dfs(0, j + 1, pacific_reachable)
            dfs(m - 1, j, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))

if __name__ == '__main__':
    s = Solution()
    s.pacificAtlanticBfs([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
