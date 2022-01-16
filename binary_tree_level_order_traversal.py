from typing import Optional, List

from common.treenode import TreeNode


class Solution:
    def levelOrderRecursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time: n
        space: n
        """
        levels = []

        if not root:
            return levels

        def bfs(node: TreeNode, level: int):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)


        bfs(root, 0)
        return levels

    def levelOrderIterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time: n
        space: n
        """
        levels = []

        if not root:
            return levels

        q = [(root, 0)]
        while q:
            node, level = q.pop(0)

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return levels