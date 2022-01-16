class Solution:
    def numTrees(self, n):
        """
        time: n^2
        space: n
        """
        numTree = [0] * (n + 1)
        numTree[0], numTree[1] = 1, 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                numTree[nodes] += numTree[root - 1] * numTree[nodes - root]

        return numTree[n]


if __name__ == '__main__':
    s = Solution()
    assert s.numTrees(1) == 1
    assert s.numTrees(2) == 3
    assert s.numTrees(3) == 5
