# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from common.treenode import TreeNode


class Solution:
    def recoverTreeInorder(self, root: Optional[TreeNode]) -> None:
        """
        time: n
        space: n
        """
        # obtain inorder traversal
        order = []
        self._dfsInorder(root, order)

        # find two out of order nodes
        first = second = None
        for i in range(len(order) - 1):
            if order[i].val > order[i + 1].val and not first:
                first = order[i]
            if order[i].val > order[i + 1].val and first:
                # second may be set twice, as second could be the following number or a later number
                second = order[i + 1]

        # swap two out of order nodes
        first.val, second.val = second.val, first.val

    def _dfsInorder(self, root: TreeNode, order: List[TreeNode]):
        if root is None:
            return

        self._dfsInorder(root.left, order)
        order.append(root)
        self._dfsInorder(root.right, order)

    def recoverTreeInorderIterative(self, root: Optional[TreeNode]) -> None:
        """
        time: n
        space: n
        """
        stack = []

        first = second = pred = None

        while stack or root:
            # go left
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pred and root.val < pred.val:
                second = root
                if first is None:
                    first = pred
                else:
                    break

            pred = root  # pred will be "parent of right child", or "root.left" if right child doesn't exist
            root = root.right

        first.val, second.val = second.val, first.val


    def recoverTreeInorderRecursive(self, root: Optional[TreeNode]) -> None:
        """
        time: n
        space: n
        """
        first = second = pred = None

        def helper(root: TreeNode):
            nonlocal first, second, pred

            if root is None:
                return

            # left
            helper(root.left)

            # self
            if pred and root.val < pred.val:
                second = root
                if not first:
                    first = pred
                else:
                    return
            pred = root

            # right
            helper(root.right)

        helper(root)
        first.val, second.val = second.val, first.val

    