from typing import List

from common.treenode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return [[]]
        return self.dfs(1, n + 1)

    def dfs(self, start: int, end: int) -> List[TreeNode]:
        if start == end:
            return None

        ans = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    ans.append(node)
        return ans