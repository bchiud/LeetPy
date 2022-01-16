from collections import deque

from common.treenode import TreeNode


class Solution:
    """
    time: n
    space: n    (log n if tree is balanced)
    """
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def dfs(root: TreeNode) -> int:
            nonlocal diameter

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(diameter, left + right)

            return max(left, right) + 1

        dfs(root)
        return diameter

    """
    time: n
    space: n
    """
    def diameterOfBinaryTreeIterative(self, root: TreeNode) -> int:
        return 0
        # TODO:




if __name__ == '__main__':
    s = Solution()

    aLr = TreeNode(5)
    aLl = TreeNode(4)
    aR = TreeNode(3)
    aL = TreeNode(2, aLl, aLr)
    aRoot = TreeNode(1, aL, aR)
    assert s.diameterOfBinaryTree(aRoot) == 3

    # assert s.diameterOfBinaryTreeIterative(aRoot) == 3