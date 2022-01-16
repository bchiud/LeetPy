from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1

        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i - 1][0] == 1 and obstacleGrid[i][0] == 0)

        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j - 1] == 1 and obstacleGrid[0][j] == 0)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[m - 1][n - 1]

if __name__ == '__main__':
    s = Solution()
    assert s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
    assert s.uniquePathsWithObstacles([[0,1],[0,0]]) == 1
    assert s.uniquePathsWithObstacles([[0,0],[0,1]]) == 0