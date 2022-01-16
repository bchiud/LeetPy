from collections import deque
from typing import List


class Solution:
    """
    bfs is space min(m, n), while dfs will be space (m * n)

    bfs will explore the first added (closest) node first, while dfs will explore last added (furthest) node first

    bfs example:
    - 3x100 grid
    - worst case starts from the middle of the grid
    the grid will be processed by expanding in a dimaond shape from the middle, bound by the shorter side
    ......QXXXQ.........
    .....QXXXXXQ........
    ......QXXXQ.........
    """

    def numIslandsBfsIterative(self, grid: List[List[str]]):
        """
        time: m * n
        space: min(m, n)
        """
        rowLen, colLen, islands = len(grid), len(grid[0]), 0

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == '1':
                    islands += 1
                    grid[row][col] = '0'
                    queue = deque([(row, col)])
                    while queue:
                        i, j = queue.popleft()
                        for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                            if 0 <= ii < rowLen and 0 <= jj < colLen and grid[ii][jj] == '1':
                                grid[ii][jj] = '0'
                                queue.append((ii, jj))

        return islands

    def numIslandsDfsRecursive(self, grid: List[List[str]]) -> int:
        """
        time: m * n
        space: m * n
        :param grid:
        :return:
        """
        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    islands += 1
                    self._exploreIsland(grid, row, col)

        return islands

    def _exploreIsland(self, grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col] == '1':
            grid[row][col] = '0'
            self._exploreIsland(grid, row - 1, col)
            self._exploreIsland(grid, row, col - 1)
            self._exploreIsland(grid, row + 1, col)
            self._exploreIsland(grid, row, col + 1)

    def numIslandsUF(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = sum(grid[i][j] == '1' for i in range(rows) for j in range(cols))

        parent = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append((i, j))
            parent.append(row)

        def find(i, j):
            if parent[i][j] != (i, j):
                return find(parent[i][j][0], parent[i][j][1])
            return parent[i][j]

        def union(x_i, x_j, y_i, y_j):
            nonlocal islands
            x_parent_i, x_parent_j, y_parent_i, y_parent_j = find(x_i, x_j), find(y_i, y_j)

            if x_parent_i == y_parent_i and x_parent_j == y_parent_j:
                return

            parent[x_i][x_j] = parent[y_i][y_j]
            islands -= 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    continue
                if i < rows - 1 and grid[i + 1][j] == '1':
                    union(i, j, i + 1, j)
                if j < cols - 1 and grid[i][j + 1] == '1':
                    union(i, j, i, j + 1)

        return islands


if __name__ == '__main__':
    s = Solution()

    assert s.numIslandsBfsIterative([["1", "1", "1", "1", "0"],
                                     ["1", "1", "0", "1", "0"],
                                     ["1", "1", "0", "0", "0"],
                                     ["0", "0", "0", "0", "0"]]) == 1
    assert s.numIslandsBfsIterative([["1", "1", "1"],
                                     ["0", "1", "0"],
                                     ["1", "1", "1"]]) == 1

    # assert s.numIslandsDfsRecursive([["1", "1", "1", "1", "0"],
    #                                  ["1", "1", "0", "1", "0"],
    #                                  ["1", "1", "0", "0", "0"],
    #                                  ["0", "0", "0", "0", "0"]]) == 1
    # assert s.numIslandsDfsRecursive([["1", "1", "1"],
    #                                  ["0", "1", "0"],
    #                                  ["1", "1", "1"]]) == 1

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(list(q))
